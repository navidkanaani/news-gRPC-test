from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaConsumer


def clean_topic_name(topic):
    """
    Clean topic name from special characters or spaces. Convert it to alphanumeric.
    STYLE & BEAUTI -> stylebeauti
    """
    clean_topic = topic.replace(' ', '_')
    clean_topic = ''.join(e for e in topic if e.isalnum())
    return clean_topic


def check_existance(topic):
    """
    Check whether a topic is already existed or not.
    """
    consumer = KafkaConsumer(bootstrap_servers="localhost:9092")
    existed_topics = consumer.topics()
    if topic not in existed_topics:
        return True
    else:
        return False


def create_topic(topics):
    """
    Create a list of given topics in kafka server.
    """
    new_topics = []
    # Check whether a topic is not existed before
    for topic in topics:
        # Clean topic name
        topic = clean_topic_name(topic)
        # Check existance of a topic
        if check_existance(topic):
            new_topics.append(topic)
    # Add new topics to Kafka
    admin = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id="admin-kaen")
    topic_list = []
    for topic in new_topics:
        topic_list.append(NewTopic(name=topic, num_partitions=1, replication_factor=1))
    admin.create_topics(new_topics=topic_list, validate_only=False)
    print("Create new topics in the Kafka broker...")