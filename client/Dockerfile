FROM phusion/baseimage

RUN apt-get update && apt-get install -y dnsutils
RUN apt-get install -y python python-scapy

RUN curl https://bootstrap.pypa.io/get-pip.py > /tmp/get-pip.py
RUN python /tmp/get-pip.py
RUN pip install dnslib
RUN pip install IPy
RUN pip install IPython

ADD set_dns /etc/my_init.d/set_dns
ADD sniff.py /root/sniff.py

