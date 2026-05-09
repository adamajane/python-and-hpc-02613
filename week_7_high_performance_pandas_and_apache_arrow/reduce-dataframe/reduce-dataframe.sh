#! /bin/bash
#BSUB -J reduce-dataframe
#BSUB -q hpc
#BSUB -W 5
#BSUB -n 1
#BSUB -R "rusage[mem=4GB]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -o reduce-dataframe_%J.out
#BSUB -e reduce-dataframe_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

python -u reduce-dataframe.py
