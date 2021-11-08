from datetime import timedelta

from airflow import DAG
from airflow.providers.amazon.aws.operators.emr_create_job_flow import EmrCreateJobFlowOperator
from airflow.providers.amazon.aws.sensors.emr_job_flow import EmrJobFlowSensor
from airflow.utils.dates import days_ago

# [START howto_operator_emr_automatic_steps_config]
SPARK_STEPS = [
    {
        'Name': 'calculate_pi',
        'ActionOnFailure': 'CONTINUE',
        'HadoopJarStep': {
            'Jar': 'command-runner.jar',
            'Args': ['/usr/lib/spark/bin/run-example', 'SparkPi', '10'],
        },
    }
]

JOB_FLOW_OVERRIDES = {
    'Name': 'PiCalc',
    'ReleaseLabel': 'emr-5.29.0',
    'Applications': [{'Name': 'Spark'}],
    'Instances': {
        'InstanceGroups': [
            {
                'Name': 'Primary node',
                'Market': 'SPOT',
                'InstanceRole': 'MASTER',
                'InstanceType': 'm1.medium',
                'InstanceCount': 1,
            }
        ],
        'KeepJobFlowAliveWhenNoSteps': False,
        'TerminationProtected': False,
    },
    'Steps': SPARK_STEPS,
    'JobFlowRole': 'iam_emr_profile_role',
    'ServiceRole': 'iam_emr_service_role',
}
# [END howto_operator_emr_automatic_steps_config]

with DAG(
    dag_id='emr_job_flow_automatic_steps_dag',
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'email': ['reynaldomendezr3@gmail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
    },
    dagrun_timeout=timedelta(hours=1),
    start_date=days_ago(1),
    schedule_interval='@once',
    tags=['example'],
) as dag:

    # [START howto_operator_emr_automatic_steps_tasks]
    job_flow_creator = EmrCreateJobFlowOperator(
        task_id='create_job_flow',
        job_flow_overrides=JOB_FLOW_OVERRIDES,
        aws_conn_id='aws_default',
        emr_conn_id='emr_default',
    )

    job_sensor = EmrJobFlowSensor(
        task_id='check_job_flow',
        job_flow_id=job_flow_creator.output,
        aws_conn_id='aws_default',
    )
    # [END howto_operator_emr_automatic_steps_tasks]

    # Task dependency created via `XComArgs`:
    #   job_flow_creator >> job_sensor