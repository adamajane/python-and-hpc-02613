#! /bin/bash
#BSUB -J cache-job-script
#BSUB -q hpc
#BSUB -W 10
#BSUB -n 1
#BSUB -R "rusage[mem=2GB]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -o cache-job-script_%J.out
#BSUB -e cache-job-script_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

python -u cache.py
