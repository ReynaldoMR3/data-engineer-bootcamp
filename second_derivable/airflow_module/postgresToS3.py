from datetime import datetime
from airflow import DAG
import airflow.utils.dates
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from airflow.providers.amazon.aws.operators.s3_list import S3ListOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator


default_args = {
    'owner' : 'reynaldo.mendez',
    'depends_on_past' : False,
    'start_date' : airflow.utils.dates.days_ago(1),
    'email' : ["reynaldomendezr3@gmail.com"],
    'email_on_failure' : True,
    'email_on_retry' : True,
    'retries' : 1,
    'retry_delay' : timedelta(minutes=5)
} 

with DAG(
    dag_id='postgres_to_s3_tasks',
    default_args=default_args,
    schedule_interval='@once'
) as dag:
    create_postgres_extension = PostgresOperator(
        task_id="create_aws_s3_extension",
        postgres_conn_id='postgres_default',
        sql="""
            CREATE EXTENSION IF NOT EXISTS aws_s3 CASCADE;
          """
    )

    export_table_to_s3 = PostgresOperator(
        task_id="postgres_to_s3",
        postgres_conn_id='postgres_default',
        sql="""
           SELECT *
           FROM aws_s3.query_export_to_s3('SELECT * FROM user_purchase', aws_commons.create_s3_uri('staging', 'user_purchase','us-east-2'));  
          """
    )

    s3_file = S3ListOperator(
    task_id='list_s3_files',
    bucket='staging',
    prefix='',
    delimiter='/',
    aws_conn_id='default_aws_conn'
    )
    create_postgres_extension >> export_table_to_s3 >> s3_file
    





