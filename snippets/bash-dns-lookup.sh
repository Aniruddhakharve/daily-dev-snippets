#!/bin/bash

DOMAIN=$1

echo "🔍 DNS Lookup for $DOMAIN"
nslookup $DOMAIN
