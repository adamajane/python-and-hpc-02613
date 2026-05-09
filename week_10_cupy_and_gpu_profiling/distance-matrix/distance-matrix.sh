#! /bin/bash
#BSUB -J distance-matrix
#BSUB -q c02613
#BSUB -W 10
#BSUB -n 1
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -R "rusage[mem=4GB]"
#BSUB -o distance-matrix_%J.out
#BSUB -e distance-matrix_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

INPUT=/dtu/projects/02613_2025/data/locations/locations_5000.csv

time python -u distance-matrix.py "$INPUT" oneloop
time python -u distance-matrix.py "$INPUT" noloop
