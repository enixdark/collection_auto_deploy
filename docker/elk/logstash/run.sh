#!/bin/sh

LOGSTASH_PORT=${LOGSTASH_PORT:-5000}
# ELASTICSEARCH_PORT=${ELASTICSEARCH_PORT:-9200}

echo 
sed -i "s/{{LOGSTASH_PORT}}/${LOGSTASH_PORT}/" /etc/logstash/conf.d/logstash.conf
sed -i "s/{{ELASTICSEARCH_URI}}/${ELASTICSEARCH_URI}/" /etc/logstash/conf.d/logstash.conf
sed -i "s/{{ELASTICSEARCH_USERNAME}}/${ELASTICSEARCH_USERNAME}/" /etc/logstash/conf.d/logstash.conf
sed -i "s/{{ELASTICSEARCH_PASSWORD}}/${ELASTICSEARCH_PASSWORD}/" /etc/logstash/conf.d/logstash.conf

# cat  /etc/logstash/conf.d/logstash.conf
exec logstash -f /etc/logstash/conf.d/logstash.conf
