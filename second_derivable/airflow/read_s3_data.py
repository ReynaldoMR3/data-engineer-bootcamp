from airflow import DAG
import airflow.utils.dates
from datetime import datetime, timedelta


default_args = {
    'owner' : 'reynaldo.mendez',
    'depends_on_past' : False,
    'start_date' : airflow.utils.dates.day_ago(1),
    'email' : ["reynaldomendezr3@gmail.com"],
    'email_on_failure' : True,
    'email_on_retry' : True,
    'retries' : 1,
    'retry_delay' : timedelta(minutes=5)
} 

dag = DAG('dag_read_s3_data', default_args=default_args, schedule_interval='@once')

