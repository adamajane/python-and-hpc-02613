#! /bin/bash
#BSUB -J pyarrow-load-and-convert
#BSUB -q hpc
#BSUB -W 5
#BSUB -n 1
#BSUB -R "rusage[mem=4GB]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -o pyarrow-load-and-convert_%J.out
#BSUB -e pyarrow-load-and-convert_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

python -u pyarrow-load-and-convert.py
