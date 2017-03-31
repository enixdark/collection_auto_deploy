FROM logstash:latest
MAINTAINER quandc "cqshinn92@gmail.com"

ADD ./conf.d /etc/logstash/conf.d
ADD ./patterns.d /etc/logstash/patterns.d
ADD ./run.sh /opt/run.sh
RUN chmod +x /opt/run.sh
# RUN logstash-plugin install x-pack
ENTRYPOINT ["/opt/run.sh"]
