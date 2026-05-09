#! /bin/bash
#BSUB -J add-kernel
#BSUB -q c02613
#BSUB -W 5
#BSUB -n 1
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -R "rusage[mem=2GB]"
#BSUB -o add-kernel_%J.out
#BSUB -e add-kernel_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

python -u add-kernel.py
