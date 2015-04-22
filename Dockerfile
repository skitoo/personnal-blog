FROM debian:wheezy
MAINTAINER Alexis Couronne


RUN apt-get update -y
RUN apt-get install -y nginx python python-pip

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN make html
RUN cp /app/nginx/default /etc/nginx/sites-available/default

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
