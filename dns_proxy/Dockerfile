FROM phusion/baseimage

RUN apt-get update && apt-get install -y dnsutils python
RUN curl https://bootstrap.pypa.io/get-pip.py > /tmp/get-pip.py
RUN python /tmp/get-pip.py
RUN pip install dnslib
RUN pip install IPy
ADD dnschef.py /usr/bin/dnschef.py

