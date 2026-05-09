#! /bin/bash
#BSUB -J gpu-job-script
#BSUB -q c02613
#BSUB -W 5
#BSUB -n 1
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -R "rusage[mem=2GB]"
#BSUB -r "span[hosts=1]"
#BSUB -o gpu-job-script_%J.out
#BSUB -e gpu-job-script_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

python -u gpu-program.py
