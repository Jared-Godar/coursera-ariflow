# Library imports

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import datetime as dt

# DAG arguments

default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2022, 9, 12),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

# DAG definition

dag = DAG('simple_example',
          description='Simple tutorial DAG',
          default_args=default_args,
          schedule_interval=dt.timedelta(seconds=5),
          )

# Task definitions

task1 = BashOperator(
    task_id='print_hello',
    bash_command='echo \'Greetings. The date and time are \'',
    dag=dag,
)

task2 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

# Task pipeline

task1 >> task2
