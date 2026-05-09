#! /bin/bash
#BSUB -J matrix-multiplication-job-script
#BSUB -q hpc
#BSUB -W 30
#BSUB -n 8
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=4GB]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -o matrix-multiplication-job-script_%J.out
#BSUB -e matrix-multiplication-job-script_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

export OMP_NUM_THREADS=8
export OPENBLAS_NUM_THREADS=8
export MKL_NUM_THREADS=8
export MPI_NUM_THREADS=8

python -u matmuls.py
