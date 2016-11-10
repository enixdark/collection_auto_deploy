
CONFIG  = {
  "namespace": "default",
  "domain": "cluster.local",
  "public_ip": '\"192.168.99.100\"',
  "docker_registry_key": "key",

  "rabbitmq": {
    "name":"rabbitmq",
    "host": '\"192.168.99.100\"',
    "port": 5672,
    "user": "rabbit_mailship",
    "pass": "rabbit_password",
    "replicas_number": 1,

    "haraka":{
      "exchange":"sender_processor",
      "exchange_type": "direct",
      "m_worker_tls": False,
      "queue":"sender_processor",
      "delivery_mode": 2,
      "durable": True,
      "auto_delete": False,
      "confirm": True,
      "routing":'"#"'
    },
    "logstash":{
      "exchange": "postfixlog",
      "exchange_type": "fanout"
    }
  },
  "redis":{
    "name":"redis",
    "host": '\"192.168.99.100\"',
    "port": 6379,
    "pass": "redis_password",
    "db": 0,
    "replicas_number": 1
  },
  "mysql":{
    "name": "mysql",
    "host": '\"192.168.99.100\"',
    "user": "root",
    "pass": "mypass",
    "port": 3306,
    "storage": '"2Gi"',
    "mountPath": "/var/lib/mysql",
    "volumeName": "db-dir",    
    "replicas_number": 1,
    "pv_name": "mysql-mailship",
    "pv_path":"/tmp/mysql",
    "pv_accessModes": ["ReadWriteOnce"],
    "persistentVolumeReclaimPolicy": "Retain",
    "pvc_name": "mysql-pvc",
    "pvc_accessModes": ["ReadWriteOnce"],


  },

  "kong":{
    "name": "kong",
    "replicas_number": 1,
    "host":  '\"192.168.99.100\"',
    "admin_api_port": 8001,
    "default_api_port": 8000,
    "default_ssl_api_port": 8443,
    "cluster_port": 7942,
    "user": "kong",
    "password": "kong",
    "database": "kong",
    "database_type": "postgres"
  },

  "mongodb":{
    "name": "mongodb",
    "host": '\"192.168.99.100\"',
    "port": 27017,
    "user": "user",
    "password": "password",
    "database": "database",
    "engine_storage": "",
    "replicas_number": 1
  },

  "postgres":{
    "name": "kong-database",
    "host": '\"192.168.99.100\"',
    "user": "kong",
    "password": "kong",
    "port": 5432,
    "database": "kong",
    "storage": '"2Gi"',
    "mountPath": "/var/lib/postgresql",
    "volumeName": "db-dir",    
    "replicas_number": 1,
    "pv_name": "postgres-pv",
    "pv_path":"/tmp/postgres",
    "pv_accessModes": ["ReadWriteOnce"],
    "persistentVolumeReclaimPolicy": "Retain",
    "pvc_name": "postgres-pvc",
    "pvc_accessModes": ["ReadWriteOnce"],
  },

  "auth":{
    "name": "auth",
    "host": '\"192.168.99.100\"',
    "port": 9296,
    "replicas_number": 1,
    "database": "auth"
  },
  "account":{
    "name": "account",
    "host": '\"192.168.99.100\"',
    "port": 9295,
    "replicas_number": 1,
    "database": "account"
  },
  "domain":{
    "name": "domain",
    "host": '\"192.168.99.100\"',
    "port": 9294,
    "replicas_number": 1,
    "database": "domain"
  },
  "email":{
    "name": "email",
    "host": '\"192.168.99.100\"',
    "port": 9293,
    "replicas_number": 1,
    "database": "email"
  },
  "log":{
    "name": "log",
    "host": '\"192.168.99.100\"',
    "port": 9297,
    "replicas_number": 1,
    "database": "log"
  },
  "verificator":{
    "name": "verificator",
    "host": '\"192.168.99.100\"',
    "port": 9298,
    "replicas_number": 1,
    "storage": '"2Gi"',
    "mountPath": "usr/local/verificator/dkim",
    "volumeName": "db-dir",    
    "replicas_number": 1,
    "pv_name": "domain-pv",
    "pv_path":"/etc/docker-ple/opendkim",
    "pv_accessModes": ["ReadWriteOnce"],
    "persistentVolumeReclaimPolicy": "Retain",
    "pvc_name": "domain-pvc",
    "pvc_accessModes": ["ReadWriteOnce"],
  },
  "validator":{
    "name": "validator",
    "host": '\"192.168.99.100\"',
    "port": 9299,
    "replicas_number": 1,
  },
  "worker":{
    "name":"worker",
    "host": '\"192.168.99.100\"',
    "preprocessor_queue":"processing_dev",
    "sender_queue":"sending_dev",
    "smpt_port":25,
    "smpt_tls_port":587,
    "smtp_host":"",
    "smtp_domain":"",
    "smtp_user":"",
    "smtp_password":"",
    "smtp_tls":""
  },
  "elk":{
    "name": "elk",
    "host": '\"192.168.99.100\"',
    "beat_port": 5044,
    "kibana_port": 5601,
    "logstash_port": 5000,
    "elasticsearch_port": 9200,
    "replicas_number": 1,
    "es_heap_size": "2g",
    "ls_heap_size": "1g"
  },
  "haraka":{
    "host": '\"192.168.99.100\"',
    "name":"haraka",
    "replicas_number": 1,
    "smtp_port": 25,
    "smtp_tls_port": 587
  },
  "postfix_log_worker":{
    "host": '\"192.168.99.100\"',
    "name": "postfix-log-worker",
    "replicas_number": 1
  },
  "postfix":{
    "name": "postfix",
    "replicas_number": 1,
    "smtp_port": 25,
    "smtp_tls_port": 587,
    "host": '\"192.168.99.100\"',
    "list_ips": "127.0.0.1",
    "myhostname": "",
    "domain": "",
    "key_file": "",
    "cert_file": ""
  },
  "logstash":{
    "name": "logstash",
    "port": 5000,
    "replicas_number": 1,
    "host": '\"192.168.99.100\"',
    "heap_size": "1024m"
  }
}
