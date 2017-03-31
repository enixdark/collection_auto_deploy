# FROM kibana:4.6
FROM kibana:latest
MAINTAINER quandc "cqshinn92@gmail.com"
RUN kibana-plugin install x-pack

ADD ./conf/kibana.yml /usr/share/kibana/config/kibana.yml
ADD ./run.sh /opt/run.sh
RUN chmod +x /opt/run.sh
ENTRYPOINT ["/opt/run.sh"]
