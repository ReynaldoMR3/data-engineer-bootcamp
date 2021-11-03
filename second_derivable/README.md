Second Deliverable (due October 31st, 11:59 PM)

Based on the self-study material, recorded and live session, and mentorship covered until this deliverable, we suggest you perform the following:
Use your up and running Airflow Cluster to create your DAGs. 
Think about the best way to design your data pipeline. Remember to include new concepts you are learning in previous weeks.
Use terraform blocks to set up your environment, you will need to create a new PostgreSQL DB with one table named user_purchase. (PostgreSQL_Table_Schema.png)
Use Airflow to upload the user_purchase.csv file into the new PostgreSQL table. Rememer there's more than 1 way to complete this step.

Outcome:
PostgreSQL table named user_purchase.
Airflow job to load user_purchase.csv in user_purchase table.
Terraform blocks to create PostgreSQL DB and table. Also, IAM needed to integrate Airflow Cluster and SQL service.
(Optional) Automation process to run Terraform blocks as part of the main Data Pipeline

To start you must follow the steps on the first derivable to start the airflow service.

Important: Change the values.yaml on the first derivable project with this github repo path to use the .py files as dags


##### TODO: FINISH IAM MODULE

Lesson Learned: Don't waste to much time learning terraform if you don't want to be a SRE.

Then follow this steps:

1. Go to the link https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/_modules/airflow/providers/amazon/aws/transfers/s3_to_redshift.html#AVAILABLE_METHODS

This will help us create our s3 to postgress operator, so we are copying the source code of the operator s3 to redshift.

Lesson learned: Start building from a similar solution.
Lesson learned: Make sure you are seeing the docs version from the version you are using.

2. Copy all the code that's on the link and paste it in a new .py file, for this example the code will be on custom_modules/transfer_s3_to_postgres.py

3. Adapt the code we just copy to our needs. # TODO: Test pandas.Dataframe.to_sql() using the connection uri from airflow connections.

4. Setup connections with the airflow UI interface. ### TODO: test IAM role and read Eiffel documentation that he shared.









