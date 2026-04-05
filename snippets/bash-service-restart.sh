#!/bin/bash

SERVICE=$1

sudo systemctl restart $SERVICE

echo "🔄 Restarted $SERVICE"
