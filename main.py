import os
import urllib.request, requests
import shutil, kafka, logging, time, datetime

def main_loop():
    files = []
    print('Streams initiated...')
    while True:
        consumer_received = kafka.KafkaConsumer('file-received', bootstrap_servers='my-cluster-kafka-bootstrap:9092', consumer_timeout_ms=10000)
        for message in consumer_received:
            str_message = print(bytes.decode(message.value))
            print(str_message)
            #if its stupid but it works...  well this is still stupid
            filename = str(str_message.split(': ')[1:])
            filename = filename.replace("'", '')
            filename = filename.replace('[', '')
            filename = filename.replace(']', '')
            files.append(filename)

            if len(files) == 2:
                get_files(files)
                files = []


def get_files(files):
    for file in files:
        print('retrieving file from dropoff pod ' + file)
        baseurl = "http://dropoff-marlowkart.apps.lakitu.hosted.labgear.io/files/"
        url = baseurl + file
        print(url)
        dlpath = '/root/downloads/'
        dlpathwithfile = dlpath + file
        r = requests.get(url)
        open(dlpathwithfile, 'wb').write(r.content)

    process_training_files(files)
    pass


def process_training_files(files):
    dlpath = '/root/downloads/'
    processingpath = '/root/processing/'
    processedpath = '/root/processed/'
    for file in files:
        shutil.move(dlpath + file, processingpath + file)


    #for timestamping results file
    now = datetime.datetime.now()
    dt_string = now.strftime("%d%m%Y-%H%M%S")

    #issue ML commands
    #####JUST A STUBOUT
    temp_file = open("/root/results/results--" + dt_string + '.txt', "w")
    temp_file.write("This is an empty results file")
    temp_file.close()
    results_file = 'results--' + dt_string + '.txt'
    ###end stubout

    send_file(results_file)
    pass


def send_file(file):
    uploadapiurl = 'http://dropoff-marlowkart.apps.lakitu.hosted.labgear.io/api-upload'
    resultsbasepath = '/root/results/'
    resultsfullpath = resultsbasepath + str(file)
    myfile = {'file': open(resultsfullpath, 'rb')}
    response = requests.post(uploadapiurl, files=myfile)
    if response.status_code == 201:
        print('results file ' + file + ' successfully sent to dropoff pod')
    else:
        print('something went wrong, try again')
    pass

if __name__ == "__main__":
    main_loop()

