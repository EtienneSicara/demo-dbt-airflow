"""
The purpose of this DAG is to test that Airflow has been correctly deployed and works
as expected: ends with success.
"""


# Required python packages
from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow import DAG
from airflow.models.baseoperator import chain
from airflow.operators.bash import BashOperator

# Arguments required by the DAG
default_args = {
    "owner": "admin",  # Owner of the dag
    "start_date": days_ago(1),  # Start the process yesterday (for immediate execution)
    "schedule_interval": None,  # Set to None to not schedule the DAG
    "depends_on_past": False,  # Dependence of previous attempts
    "retries": 1,  # Limit of the number of retries
    "retry_delay": timedelta(minutes=1),  # Retry after 1 minute
}

# Initiate a DAG
with DAG(
    dag_id="airflow-test",
    default_args=default_args,
) as dag:
    # Define a task (node). Here it runs the bash command "echo hello"
    hello = (
        BashOperator(
            task_id="echo_hello",
            bash_command="echo hello",
            dag=dag,
        ),
    )

    world = BashOperator(
        task_id="echo_world",
        bash_command="echo world",
        dag=dag,
    )

    # The function chain builds the DAG. Here: 'hello' -> 'world'
    # To build task in parallel, one can use []
    # Ex: 'hello' -> ['world', 'random_task'] <=> chain(hello, [world, random_task])
    chain(hello, world)
