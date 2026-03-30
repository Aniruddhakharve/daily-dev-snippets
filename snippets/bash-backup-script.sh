#!/bin/bash

# 📦 Backup Script

SOURCE=$1
DEST=$2

tar -czvf "$DEST/backup_$(date +%F).tar.gz" "$SOURCE"

echo "✅ Backup completed"
