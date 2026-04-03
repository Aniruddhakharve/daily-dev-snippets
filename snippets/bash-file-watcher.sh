#!/bin/bash

FILE=$1

echo "👀 Watching $FILE for changes..."

while true
do
  inotifywait -e modify $FILE
  echo "File modified!"
done
