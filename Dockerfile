FROM debian:wheezy
MAINTAINER Alexis Couronne


RUN apt-get update -y
RUN apt-get install -y python python-pip

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN make html

VOLUME ["/app/output"]
