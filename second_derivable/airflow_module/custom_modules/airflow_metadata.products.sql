CREATE TABLE IF NOT EXISTS airflow_metadata.user_purchase 
(
    id SERIAL PRIMARY KEY,
    invoice_number varchar(10),
    stock_code varchar(20),
    detail varchar(1000),
    quantity int,
    invoice_date timestamp,
    unit_price numberic(8,3),
    customer_id int,
    country varchar(20)
);