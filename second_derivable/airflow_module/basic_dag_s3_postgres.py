from datetime import datetime
from airflow import DAG
import airflow.utils.dates
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta
from airflow.hooks.postgres_hook import PostgresHook

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

def read_postgres_data():
    request = "SELECT * FROM user_purchase LIMIT 10;"
    pg_hook = PostgresHook(postgres_conn_id='postgres_default')
    connection = pg_hook.get_conn()
    cursor = connection.cursor()
    cursor.execute(request)
    sources = cursor.fetchall()
    for source in sources:
        print(f"{source}")
    return sources


with DAG(
    dag_id='s3_to_postgres_tasks',
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
    create_users_table = PostgresOperator(
        task_id="create_users_tables",
        postgres_conn_id='postgres_default',
        sql="""
            CREATE TABLE IF NOT EXISTS user_purchase 
                (
                    id SERIAL PRIMARY KEY,
                    invoice_number varchar(10),
                    stock_code varchar(20),
                    detail varchar(1000),
                    quantity int,
                    invoice_date timestamp,
                    unit_price numeric(8,3),
                    customer_id int,
                    country varchar(20)
                );
          """
    )

    populate_table = PostgresOperator(
        task_id="populate_users_tables",
        postgres_conn_id='postgres_default',
        sql="""
            SELECT aws_s3.table_import_from_s3('user_purchase', '', 'DELIMITER ''|''', aws_commons.create_s3_uri('second-derivable20211101213449672200000001', 'user_purchase.txt', 'us-east-2') );
          """
    )
    read_data = PythonOperator(task_id='read_data', python_callable=read_postgres_data)

    create_postgres_extension >> create_users_table >> populate_table >> read_data