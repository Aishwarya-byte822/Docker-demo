from kafka import KafkaProducer
import json
import time
import random

def run_producer():
    producer = KafkaProducer(
        bootstrap_servers=['kafka:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    user_ids = [101, 102, 103, 104, 105]

    print("Airflow triggered producer...")

    for i in range(20):
        tx_data = {
            "tx_id": i,
            "userId": random.choice(user_ids),
            "amount": random.uniform(10.0, 15000.0),
            "timestamp": time.time()
        }

        producer.send('fraud-detection', value=tx_data)
        print(f"Sent: {tx_data}")
        time.sleep(1)

    producer.flush()
    producer.close()
