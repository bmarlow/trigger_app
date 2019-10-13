import os
import urllib.request
import shutil, kafka, logging, time

def main_loop():
    count = 0
    files = []
    while True:
        consumer_received = kafka.KafkaConsumer('file-received', bootstrap_servers='my-cluster-kafka-bootstrap:9092', consumer_timeout_ms=10000)
        for message in consumer_received:
            print(bytes.decode(message.value))
            file = message.value.split(': ')[1:]
            files.append(file)
            if files.len() == 2:
                break
    #make API call to get files
    print('you escaped the loop!')

if __name__ == "__main__":
    main_loop()

