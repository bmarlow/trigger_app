import os
import urllib.request
import shutil, kafka, logging, time

def main_loop():
    while True:
        consumer_received = kafka.KafkaConsumer('file-received', bootstrap_servers='my-cluster-kafka-bootstrap:9092', consumer_timeout_ms=1000)
        for message in consumer_received:
            print(message.value)
        time.sleep(1)

if __name__ == "__main__":
    main_loop()

