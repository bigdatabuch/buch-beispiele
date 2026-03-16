"""
Kafka Consumer Example

This script connects to a local Apache Kafka broker and consumes messages
from a specified topic using the kafka-python client.

Features:
- Uses a consumer group for offset management
- Automatically commits offsets
- Deserializes JSON message values
- Graceful shutdown with Ctrl+C

Requirements:
    pip install kafka-python
"""

from kafka import KafkaConsumer
import json

# ------------------------------------------------------------
# Kafka connection configuration
# ------------------------------------------------------------

# Address of the Kafka broker
BOOTSTRAP = "localhost:9092"

# Kafka topic to consume from
TOPIC = "my_first_topic"

# Consumer group ID
# Kafka uses this to manage offsets and distribute partitions
GROUP_ID = "my-group-1" 


if __name__ == "__main__":
    consumer = KafkaConsumer(
        TOPIC,
        # Kafka broker address(es) to connect to
        bootstrap_servers=BOOTSTRAP,
        # Consumer group ID for offset management
        group_id=GROUP_ID,
        # If no committed offset exists for a partition, start consuming from the earliest message
        auto_offset_reset="earliest",    
        # Automatically commit offsets after processing messages
        enable_auto_commit=True,
        # Deserialize message values from JSON format
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        # Deserialize message key from bytes → string
        key_deserializer=lambda k: k.decode("utf-8") if k else None,
    )

    print("Warte auf Nachrichten... (Strg+C zum Beenden)")
    try:
        # Continuously consume messages from the topic
        for msg in consumer:
            print(
                f"Topic={msg.topic} Partition={msg.partition} Offset={msg.offset} "
                f"Key={msg.key} Value={msg.value}"
            )
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
        print("Kafka-Consumer wurde geschlossen.")

