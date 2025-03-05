#!/bin/bash
echo "Activating Conda environment..."
source /opt/conda/bin/activate myenv

echo "Running data processing scripts..."
python /app/code/src/run.py process_data --cfg /app/code/config/config.yaml --dirout /app/code/outputs/
python /app/code/src/run.py process_data_all --cfg /app/code/config/config.yaml --dirout /app/code/outputs/

echo "Processing completed!"


