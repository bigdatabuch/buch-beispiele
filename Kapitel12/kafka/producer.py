"""
Kafka Producer Example

This script reads lines from standard input (stdin) and sends them as JSON
messages to an Apache Kafka topic.

Key features:
- Connects to a Kafka broker running at localhost:9092
- Serializes message values as JSON
- Uses message keys to demonstrate partitioning
- Includes a simple retry mechanism if Kafka is not yet available
- Gracefully shuts down on Ctrl+C

Example usage:
    python producer.py
    hello world
    another message

Requirements:
    pip install kafka-python
"""

from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import json, time, sys

# address of the Kafka broker and topic name
BOOTSTRAP = "localhost:9092"
TOPIC = "my_first_topic"

def get_producer():
    # create and configure a KafkaProducer instance
    # includes JSON serialization and UTF-8 encoding for keys
    return KafkaProducer(
        # Kafka broker Address
        bootstrap_servers=BOOTSTRAP,
        # serialize message values as JSON and encode as UTF-8
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        # serialize keys as UTF-8 strings (if not None)
        key_serializer=lambda k: str(k).encode("utf-8") if k is not None else None,
        # wait up to 5ms for more messages to batch together before sending
        linger_ms=5,                
        # wait for full acknowledgment from all replicas before considering a message sent 
        acks="all",
        # retry up to 5 times if sending fails                 
        retries=5,                  
    )

if __name__ == "__main__":
    # try multiple times to connect to Kafka, with a delay between attempts
    for i in range(10):
        try:
            producer = get_producer()
            break
        except NoBrokersAvailable:
            print("Kafka noch nicht erreichbar, warte...")
            time.sleep(2)
    else:
        raise SystemExit("Kafka nicht erreichbar.")

    try: 
        # read lines from stdin, create a message with an ID and the input text, and send to Kafka
        for msg_id, line in enumerate(sys.stdin, start=1):
            # remove whitespace and newline characters from the input line
            msg = line.strip()
            # skip empty lines
            if not msg:
                continue
            # Create a JSON event structure
            event = {"id": msg_id, "msg": msg}
            # example key for partitioning
            # messages with the same key go to the same partition 
            # distributing messages across 3 partitions based on msg_id
            key = f"user-{msg_id % 3}" 
            # send the message to Kafka asynchronously (non-blocking) 
            producer.send(TOPIC, key=key, value=event)
            # print confirmation to console
            print(f"Gesendet: {event}")
    except KeyboardInterrupt:
            # triggered when the user presses Ctrl+C to stop the producer
            print("\nAbgebrochen.")
    finally:
        # ensure all messages are sent before closing the producer
        producer.flush()
        # close the producer connection
        producer.close()
        print("Fertig.")

