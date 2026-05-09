#! /bin/bash
#BSUB -J reduction-full
#BSUB -q hpc
#BSUB -W 10
#BSUB -n 4
#BSUB -R "rusage[mem=2GB]"
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -o reduction-full_%J.out
#BSUB -e reduction-full_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

python -u reduction_full.py /dtu/projects/02613_2025/data/celeba/celeba_200.npy
