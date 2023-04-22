from kafka import KafkaAdminClient
from kafka.admin import NewTopic

admin = KafkaAdminClient(bootstrap_servers="localhost:9092")

topic = NewTopic(name="message-topic", num_partitions=1, replication_factor=3)

admin.create_topics([topic])

topic = NewTopic(name="dead-letter-topic", num_partitions=1, replication_factor=3)

admin.create_topics([topic])