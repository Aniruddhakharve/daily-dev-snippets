#!/bin/bash

URL=$1

STATUS=$(curl -o /dev/null -s -w "%{http_code}\n" $URL)

echo "HTTP Status: $STATUS"
