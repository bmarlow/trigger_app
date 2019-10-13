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
            str_message = bytes.decode(message.value)
            file = str_message.split(': ')[1:]
            print(file)
            files.append(file)
            print(len(files))

            if len(files) == 2:
                get_files(files[0], files[1])
                files = []



def get_files(file1, file2):
    pass

if __name__ == "__main__":
    main_loop()

