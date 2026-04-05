#!/bin/bash

SRC=$1
DEST=$2

cp -r $SRC $DEST/backup_$(date +%F_%H-%M-%S)

echo "✅ Backup created"
