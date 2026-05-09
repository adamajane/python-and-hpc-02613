#! /bin/bash
#BSUB -J reduce
#BSUB -q c02613
#BSUB -W 5
#BSUB -n 1
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -R "rusage[mem=4GB]"
#BSUB -o reduce_%J.out
#BSUB -e reduce_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

python -u reduce.py 4000000
