FROM centos:centos7

#add my files

ADD main.py /root/

#install pre-reqs
RUN yum -y install python3 shutil wget

#install python pre-reqs
RUN pip3 install --upgrade pip
RUN pip3 install flask app requests kafka


WORKDIR /root/
CMD python3 main.py
