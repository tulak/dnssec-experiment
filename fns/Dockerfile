FROM phusion/baseimage

RUN apt-get update && apt-get install -y bind9 bind9utils bind9-doc dnsutils
ADD named.conf.options /etc/bind/named.conf.options

RUN mkdir /etc/service/bind/
ADD named_run.sh /etc/service/bind/run
RUN chmod +x /etc/service/bind/run

ADD get_host_ip /usr/local/bin/get_host_ip
ADD setup_ans /usr/local/bin/setup_ans
ADD set_forwarder_ans /usr/local/bin/set_forwarder_ans

