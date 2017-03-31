`docker pull docker-registry.vccloud.vn/lamdt/logstash`

Start container:

`docker run -d --name logstash \
           -p 1810:1810 \
           -e LS_HEAP_SIZE=1024m \
           -e LOGSTASH_PORT=1810 \
           -e RABBITMQ_HOST=127.0.0.1\
           -e IP=127.0.0.1 \
           -e RABBITMQ_PORT=5672 \
           -e RABBITMQ_USER=guest \
           -e RABBITMQ_PASS=guest \
           -e RABBITMQ_EXCHANGE=postfixlog \
           -e RABBITMQ_EXCHANGE_TYPE=fanout \
           docker-registry.vccloud.vn/lamdt/logstash
`
