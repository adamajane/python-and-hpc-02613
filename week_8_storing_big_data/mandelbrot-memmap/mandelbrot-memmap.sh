#! /bin/bash
#BSUB -J mandelbrot-memmap
#BSUB -q hpc
#BSUB -W 30
#BSUB -n 8
#BSUB -R "rusage[mem=2GB]"
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -o mandelbrot-memmap_%J.out
#BSUB -e mandelbrot-memmap_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

python -u mandelbrot-memmap.py 1000 8
