#!/bin/bash

DIR=$1

COUNT=$(ls -1 "$DIR" | wc -l)

echo "Total files: $COUNT"
