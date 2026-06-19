from kafka import KafkaConsumer
import json

user_id = int(input("Enter User ID: "))

consumer = KafkaConsumer(
    "user-alert-topic",
    bootstrap_servers=["kafka:9092"],
    auto_offset_reset="latest",
    value_deserializer=lambda x:
        json.loads(x.decode("utf-8"))
)

for message in consumer:

    data = message.value

    if data["userId"] == user_id:

        print("\n[USER ALERT]")
        print(data)