#!/bin/bash
# set -e
#cat /etc/sysctl.conf

# sysctl -p /etc/sysctl.conf
# sysctl -w vm.max_map_count=262144
# cat /proc/sys/vm/max_map_count
# echo 262144 > /proc/sys/vm/max_map_count

# unset 

elasticsearch -E network.host=0.0.0.0 -E discovery.zen.minimum_master_nodes=1

