#!/bin/bash

free_mem=$(free | grep Mem | awk '{print $4}')

echo "Free Memory: $free_mem"
