from datetime import datetime
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG(
    dag_id="postgres_operator_dag",
    start_date=datetime.datetime(2021, 11, 1),
    schedule_interval="@once",
    catchup=False,
) as dag:
    create_user_purchase_table = PostgresOperator(
        task_id="create_user_purchase_table",
        sql="""
            CREATE TABLE IF NOT EXISTS user_purchase (
            invoice_number varchar(10),
            stock_code varchar(20),
            detail varchar(1000),
            quantity int,
            invoice_date timestamp,
            unit_price numberic(8,3),
            customer_id int,
            country varchar(20)
            );
          """,
    )