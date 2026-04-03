#!/bin/bash

PROCESS=$1

pkill -f $PROCESS

echo "❌ Process killed: $PROCESS"
