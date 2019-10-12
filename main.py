import os
import urllib.request
import shutil, kafka, logging, time

def main_loop():
    while True:
        kafka.KafkaConsumer()
        consumer_received = kafka.KafkaConsumer('file-received', bootstrap_servers='my-cluster-kafka-bootstrap:9092', consumer_timeout_ms=10000)
        for message in consumer_received:
            print(bytes.decode(message.value))


if __name__ == "__main__":
    main_loop()

