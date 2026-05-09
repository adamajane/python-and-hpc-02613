#! /bin/bash
#BSUB -J total-precipitation
#BSUB -q hpc
#BSUB -W 10
#BSUB -n 1
#BSUB -R "rusage[mem=4GB]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -o total-precipitation_%J.out
#BSUB -e total-precipitation_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

python -u total-precipitation.py /dtu/projects/02613_2025/data/dmi/2023_01.csv.zip
