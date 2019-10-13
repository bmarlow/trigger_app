FROM registry.access.redhat.com/ubi7/ubi:latest

#add my files

ADD main.py /root/
RUN mkdir /root/downloads
RUN chmod 777 /root/downloads
RUN mkdir /root/results
RUN chmod 777 /root/results
RUN mkdir /root/processing
RUN chmod 777 /root/processing
RUN mkdir /root/processed
RUN chmod 777 /root/processed

#install pre-reqs
RUN yum -y --disableplugin=subscription-manager install python3 shutil wget vim

#install python pre-reqs
RUN pip3 install --upgrade pip
RUN pip3 install flask app requests kafka


WORKDIR /root/
CMD python3 -u main.py
