from datetime import datetime
from airflow import DAG
import airflow.utils.dates
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta


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
    dag_id='postgres_create_extension',
    default_args=default_args,
    schedule_interval='@once'
) as dag:
    create_postgres_extension = PostgresOperator(
        task_id="create_aws_s3_extension",
        postgress_conn_id='postgres_default',
        sql="""
            CREATE EXTENSION aws_s3 CASCADE;
          """
    )