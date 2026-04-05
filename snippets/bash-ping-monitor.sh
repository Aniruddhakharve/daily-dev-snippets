#!/bin/bash

HOST=$1

while true
do
  ping -c 1 $HOST > /dev/null && echo "UP" || echo "DOWN"
  sleep 2
done
