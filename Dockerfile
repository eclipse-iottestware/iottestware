#https://www.eclipse.org/forums/index.php/t/1094222/
FROM eclipsetitan/titan-ubuntu:6.4.0
MAINTAINER Alexander Kaiser
LABEL description="IoT-Testware CLI Image"

USER root

## PREPARE THE SYSTEM
RUN apt-get update && sudo apt-get install -y apt-utils build-essential libsctp-dev python3.6

## CLONE AND PREPARE iottestware
RUN git clone https://github.com/eclipse/iottestware && /bin/bash -c "source /etc/bash.bashrc" && sudo chmod 777 /home/titan/iottestware/install.py

## EXECUTE install.py
RUN python3.6 /home/titan/iottestware/install.py -p mqtt -b --path /home/titan/iottestware # && python3.6 /home/titan/iottestware/install.py -p coap -b --path /home/titan/iottestware

## PREPARE ADDITIONAL TOOLS
RUN apt-get install -y nmap tcpdump curl net-tools iputils-ping vim

## PREPARE THE PLAYGROUND
RUN mkdir /home/titan/playground/ && mkdir /home/titan/playground/mqtt # && mkdir /home/titan/playground/coap
WORKDIR /home/titan/playground

RUN mv /home/titan/iottestware/IoT-Testware/iottestware.mqtt/bin/iottestware.mqtt /home/titan/playground/mqtt \
		&& cp /home/titan/iottestware/IoT-Testware/iottestware.mqtt/cfg/* /home/titan/playground/mqtt \
		#&& mv /home/titan/iottestware/IoT-Testware/iottestware.coap/bin/iottestware.coap /home/titan/playground/coap \
		#&& cp /home/titan/iottestware/IoT-Testware/iottestware.coap/cfg/* /home/titan/playground/coap \
