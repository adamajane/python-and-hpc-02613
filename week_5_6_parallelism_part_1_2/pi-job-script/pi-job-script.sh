#! /bin/bash
#BSUB -J pi-job-script
#BSUB -q hpc
#BSUB -W 5
#BSUB -n 10
#BSUB -R "rusage[mem=512MB]"
#BSUB -R "select[model == XeonE5_2660v3]"
#BSUB -R "span[hosts=1]"
#BSUB -o pi-job-script_%J.out
#BSUB -e pi-job-script_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

echo "=== Serial ==="
time python -u pi_fully_serial.py

echo "=== Fully parallel ==="
time python -u pi_fully_parallel.py

echo "=== Chunked parallel ==="
time python -u pi_chunked_parallel.py
