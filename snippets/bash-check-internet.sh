#!/bin/bash

ping -c 1 google.com > /dev/null && echo "Online" || echo "Offline"
