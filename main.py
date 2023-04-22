import json

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])


def send_message(topic, data):
    producer.send(topic, json.dumps(data).encode('utf-8'))


message = {"type": "message"}
send_message("message-topic", message)

error = {"type": "error"}
send_message("message-topic", error)
producer.close()
