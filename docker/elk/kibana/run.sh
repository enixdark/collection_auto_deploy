#!/bin/sh

sed -i "s/{{KIBANA_HOST}}/${KIBANA_HOST}/" /usr/share/kibana/config/kibana.yml
sed -i "s/{{KIBANA_PORT}}/${KIBANA_PORT}/" /usr/share/kibana/config/kibana.yml
sed -i "s/{{ELASTICSEARCH_URI}}/${ELASTICSEARCH_URI}/" /usr/share/kibana/config/kibana.yml


# cat /usr/share/kibana/config/kibana.yml
kibana serve