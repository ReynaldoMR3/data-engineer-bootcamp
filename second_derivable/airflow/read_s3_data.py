from airflow import DAG
import airflow.utils.dates
from datetime import datetime, timedelta
from custom_modules.transfer_s3_to_postgres import S3ToPotsgresOperator


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

dag = DAG('dag_read_s3_data', default_args=default_args, schedule_interval='@once')

process_data = S3ToPotsgresOperator(
    task_id = 'dag_s3_to_postgres',
    schema = 'airflow_metadata',
    table = 'user_purchase',
    s3_bucket = 'second-derivable20211101213449672200000001',
    s3_key = 'user_purchase.csv',
    dag=dag
)