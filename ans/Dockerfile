FROM phusion/baseimage

RUN apt-get update && apt-get install -y bind9 bind9utils bind9-doc haveged
ADD named.conf.options /etc/bind/named.conf.options

RUN mkdir /etc/service/bind/
ADD named_run.sh /etc/service/bind/run
RUN chmod +x /etc/service/bind/run

ADD zones/example.com.zone /var/cache/bind/example.com.zone
ADD zones/example.com.zonerec /var/cache/bind/example.com.zonerec
RUN cat /var/cache/bind/example.com.zonerec >> /etc/bind/named.conf.local

ADD zones/segredes.com.zone /var/cache/bind/segredes.com.zone
ADD zones/segredes.com.zonerec /var/cache/bind/segredes.com.zonerec
RUN cat /var/cache/bind/segredes.com.zonerec >> /etc/bind/named.conf.local

ADD zones/pir.org.zone /var/cache/bind/pir.org.zone
ADD zones/pir.org.zonerec /var/cache/bind/pir.org.zonerec
RUN cat /var/cache/bind/pir.org.zonerec >> /etc/bind/named.conf.local

ADD set_ns_ip /usr/local/bin/set_ns_ip
RUN mkdir -p /etc/my_init.d 
RUN cd /etc/my_init.d/ && ln -s /usr/local/bin/set_ns_ip 01_set_ns_ip

ADD generate_keys /usr/local/bin/generate_keys
ADD sign_zones /usr/local/bin/sign_zones

