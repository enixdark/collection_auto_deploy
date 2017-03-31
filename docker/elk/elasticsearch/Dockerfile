FROM docker.elastic.co/elasticsearch/elasticsearch:5.2.1
# FROM elasticsearch:2.4
# USER root
# ENV ES_JAVA_OPTS="-Des.path.conf=/etc/elasticsearch"
ADD ./conf/elasticsearch.yml /usr/share/elasticsearch/config
# ADD ./entrypoint.sh . 
#WORKDIR /root 
#RUN chmod +x entrypoint.sh 
# RUN bin/elasticsearch-plugin install x-pack
# RUN plugin install mobz/elasticsearch-head

# RUN echo vm.max_map_count=262144 >> /etc/sysctl.conf
#RUN sysctl -p 
# RUN elasticsearch-plugin install x-pack
# RUN chown -R elasticsearch:elasticsearch entrypoint.sh
# USER elasticsearch
# CMD ["./entrypoint.sh"]
CMD ["elasticsearch", "-E", "network.host=0.0.0.0", "-E", "discovery.zen.minimum_master_nodes=1" ]
# CMD ["elasticsearch", "-D", "network.host=0.0.0.0", "-D", "discovery.zen.minimum_master_nodes=1"]
