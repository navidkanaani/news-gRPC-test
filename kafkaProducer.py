from kafkaAdmin import clean_topic_name
from kafka import KafkaProducer
import json


def kafka_producer(news):
    """
    Prepare data to store in Kafka.
    Produce searched news in kafka broker.
    """
    # Retrieve topic, key, value from data.
    topic = clean_topic_name(news['category'])  # We used category as topic name.
    message_key = bytes(news['headline'], 'utf-8')
    message_value = bytes(json.dumps(news), 'utf-8')
    # Connect to Kafka
    producer = KafkaProducer(bootstrap_servers="localhost:9092")
    print(f"Store on topic: {topic} ...")
    producer.send(topic, message_key, message_value)