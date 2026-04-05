#!/bin/bash

echo "📊 Disk Usage Summary"
df -h | grep "^/dev"
