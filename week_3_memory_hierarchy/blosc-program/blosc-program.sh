#! /bin/bash
#BSUB -J blosc-program
#BSUB -q hpc
#BSUB -W 5
#BSUB -n 1
#BSUB -R "rusage[mem=512MB]"
#BSUB -R "select[model == XeonE5_2660v3]"
#BSUB -o blosc-program_%J.out
#BSUB -e blosc-program_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026
