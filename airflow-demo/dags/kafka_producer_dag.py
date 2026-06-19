from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def test_producer():
    print("Kafka Producer DAG Triggered")

with DAG(
    dag_id="kafka_producer_dag",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task = PythonOperator(
        task_id="run_producer",
        python_callable=test_producer
    )
