#!/bin/bash

FILE=$1

echo "📡 Watching logs for ERROR..."
tail -f $FILE | grep --line-buffered "ERROR"
