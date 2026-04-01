#!/bin/bash

HOST=$1

if ping -c 1 $HOST &> /dev/null
then
  echo "✅ $HOST is reachable"
else
  echo "❌ $HOST is not reachable"
fi
