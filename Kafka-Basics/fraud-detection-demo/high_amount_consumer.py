from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "high-amount-topic",
    bootstrap_servers=["kafka:9092"],
    auto_offset_reset="latest",
    value_deserializer=lambda x:
        json.loads(x.decode("utf-8"))
)

for message in consumer:
    data = message.value

    print("\n[HIGH AMOUNT ALERT]")
    print(data)