import os
import urllib.request
import shutil, kafka, logging, time

def main_loop():
    count = 0
    files = []
    print('Streams initiated...')
    while True:
        consumer_received = kafka.KafkaConsumer('file-received', bootstrap_servers='my-cluster-kafka-bootstrap:9092', consumer_timeout_ms=10000)
        for message in consumer_received:
            print(bytes.decode(message.value))
            str_message = bytes.decode(message.value)
            file = str(str_message.split(': ')[1:])
            print(file)
            files.append(file)
            print(len(files))

            if len(files) == 2:
                get_files(files)
                files = []


def get_files(files):
    for file in files:
        print('retrieving file ' + file)
        url = "http://dropoff-marlowkart.apps.lakitu.hosted.labgear.io/files/" + file
        urllib.request.urlretrieve(url, '/root/downloads/' + file)
    pass



if __name__ == "__main__":
    main_loop()

