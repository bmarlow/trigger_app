import os
import urllib.request
import shutil, kafka, logging, time

def main_loop():
    files = []
    print('Streams initiated...')
    while True:
        consumer_received = kafka.KafkaConsumer('file-received', bootstrap_servers='my-cluster-kafka-bootstrap:9092', consumer_timeout_ms=10000)
        for message in consumer_received:
            print(bytes.decode(message.value))
            str_message = bytes.decode(message.value)
            filename = str(str_message.split(': ')[1:])
            print(filename)
            files.append(filename)
            print(len(files))

            if len(files) == 2:
                get_files(files)
                print(files)
                files = []


def get_files(files):
    for file in files:
        print('the file variable is a ' + str(type(file)))
        print('the files variable is a ' + str(type(files)))
        print('retrieving file ' + file)
        baseurl = "http://dropoff-marlowkart.apps.lakitu.hosted.labgear.io/files/"
        url = baseurl + file
        print(url)
        dlpath = '/root/downloads'
        dlpathwithfile = dlpath + file
        urllib.request.urlretrieve(url, '/root/downloads/' + dlpathwithfile)
    pass


def process_training_files(file1, file2):
    pass


def send_file(file):
    pass


if __name__ == "__main__":
    main_loop()

