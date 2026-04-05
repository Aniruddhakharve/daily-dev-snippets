#!/bin/bash

echo "Enter expression:"
read expr

result=$(echo "$expr" | bc)
echo "Result: $result"
