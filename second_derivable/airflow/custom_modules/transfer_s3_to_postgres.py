from os import defpath, replace
import warnings
from typing import List, Optional, Union

from airflow.models import BaseOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.hooks.postgres_hook import PostgresHook
from airflow.exceptions import AirflowException
from airflow.utils.decorators import apply_defaults
import pandas as pd
import io
import os



class S3ToPotsgresOperator(BaseOperator):

    template_fields = ()


    template_ext = ()


    ui_color = '#99e699'

    @apply_defaults
    def __init__(
        self,
        *,
        schema: str,
        table: str,
        s3_bucket: str,
        s3_key: str,
        postgres_conn_id: str = 'postgres_default',
        aws_conn_id: str = 's3_default',
        verify: Optional[Union[bool, str]] = None,
        wilcard_match = False,
        column_list: Optional[List[str]] = None,
        copy_options: Optional[List] = None,
        autocommit: bool = False,
        method: str = 'APPEND',
        upsert_keys: Optional[List[str]] = None,
        **kwargs,
    ) -> None:

        if 'truncate_table' in kwargs:
            warnings.warn(
                """`truncate_table` is deprecated. Please use `REPLACE` method.""",
                DeprecationWarning,
                stacklevel=2,
            )
            if kwargs['truncate_table']:
                method = 'REPLACE'
            kwargs.pop('truncate_table', None)

        super().__init__(**kwargs)
        self.schema = schema
        self.table = table
        self.s3_bucket = s3_bucket
        self.s3_key = s3_key
        self.postgres_conn_id = postgres_conn_id
        self.aws_conn_id = aws_conn_id
        self.verify = verify
        self.wildcard_match = wildcard_match
        self.column_list = column_list
        self.copy_options = copy_options or []
        self.autocommit = autocommit
        self.method = method
        self.upsert_keys = upsert_keys


    def execute(self, context) -> None:
        #Connection with postgres
        self.pg_hook = PostgresHook(postgres_conn_id = self.postgres_conn_id)

        self.s3 = S3Hook(aws_conn_id = self.aws_conn_id)

        self.log.info('Connecting...')

        if self.wildcard_match:

            if self.s3.check_for_wildcard_key(self.s3_key, self.s3_bucket):
                raise AirflowException(f"No key matches {self.s3_key}")

            s3_key_object = self.s3.get_wildcard_key(self.s3_key, self.s3_bucket)

        else:
            if not self.s3.check_for_key(self.s3_key, self.s3_bucket):
                raise AirflowException(f"No key does not exists {self.s3_key}")

            s3_key_object = self.s3.get_key(self.s3_key, self.s3_bucket)

        
        list_srt_content = s3_key_object.get()['Body'].read().decode(encoding = 'utf-8', errors = "ignore")

        schema = {
            'invoice_number' : 'string',                                          
            'stock_code' : 'string',
            'detail' : 'string',
            'quantity' : 'integer',
            'unit_price' : 'float64',
            'customer_id' : 'integer',
            'country' : 'string'
        }

        date_cols = ['invoice_date']

        df_products = pd.read_csv(io.StringIO(list_srt_content),
                                  header=0,
                                  delimiter=',',
                                  quotechar='"',
                                  low_memory=False,
                                  dtype=schema
        )

        list_df_products = df_products.values.tolist()
        list_df_products = [tuple(x) for x in list_df_products]
        self.log.info(list_df_products)

        name_file = 'airflow_metadata.products.sql'
        path_file = 'second_derivable/airflow/custom_modules/' + os.path.sep + name_file

        encode = 'UTF-8'

        with open(path_file, 'r', encoding=encode) as sql_file:
            SQL_CREATE_TBL = sql_file.read()
            sql_file.close()

            self.log.info(SQL_CREATE_TBL)

        self.pg_hook.run(SQL_CREATE_TBL)

        self.list_target_fields =  ['invoice_number',                                          
                               'stock_code',
                               'detail',
                               'quantity',
                               'unit_price',
                               'customer_id',
                               'country']

        self.current_table = self.schema + '.' + self.table

        self.pg_hook.insert_rows(self.current_table, list_df_products, target_fields=self.list_target_fields, commit_every=1000, replace=False)

        self.request = 'SELECT * FROM' + self.current_table
        self.connection = self.pg_hook.get_conn()
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.request)
        self.source = self.cursor.fetchall()

        for row in self.source:
            self.log.info(f"""invoice_number: {row[0]} -                                   
                               stock_code: {row[1]} -
                               detail: {row[2]} -
                               quantity: {row[3]} -
                               unit_price: {row[4]} -
                               customer_id: {row[5]} -
                            country: {row[6]}"""
            )

