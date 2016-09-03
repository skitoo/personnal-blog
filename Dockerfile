FROM python:3-onbuild
MAINTAINER Alexis Couronne

RUN apt-get update -y
RUN apt-get install -y locales

# Set the locale
RUN locale-gen fr_FR
RUN update-locale fr_FR

RUN pelican content/ -o /var/www/blog/ -s pelicanconf.py

VOLUME ["/usr/src/app", "/var/www/blog"]
