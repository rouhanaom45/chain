#!/bin/bash

while true; do
    # Run download.py
    python3 download.py
    
    # Wait for 2 seconds
    sleep 2

    # Run upload.py
    python3 upload.py

    # Wait for 4 minutes
    sleep 240
done
