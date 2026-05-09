#! /bin/bash
#BSUB -J save-parquet
#BSUB -q hpc
#BSUB -W 10
#BSUB -n 1
#BSUB -R "rusage[mem=4GB]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -o save-parquet_%J.out
#BSUB -e save-parquet_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

python -u save-parquet.py /dtu/projects/02613_2025/data/dmi/2023_01.csv.zip
