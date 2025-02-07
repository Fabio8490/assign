#!/bin/bash
# Script to execute the data processing program

if [ $# -eq 0 ]; then
    echo "Usage: ./run_script.sh <input_file>"
    exit 1
fi

python3 data_processor.py "$1"

# For Linux/Mac