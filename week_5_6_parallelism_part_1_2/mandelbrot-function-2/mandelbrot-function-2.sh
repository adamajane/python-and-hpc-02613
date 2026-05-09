#! /bin/bash
#BSUB -J mandelbrot-function-2
#BSUB -q hpc
#BSUB -W 5
#BSUB -n 4
#BSUB -R "rusage[mem=1GB]"
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -o mandelbrot-function-2_%J.out
#BSUB -e mandelbrot-function-2_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

python -u mandelbrot-function-2.py
