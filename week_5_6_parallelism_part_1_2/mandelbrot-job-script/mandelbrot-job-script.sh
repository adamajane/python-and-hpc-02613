#! /bin/bash
#BSUB -J mandelbrot-job-script
#BSUB -q hpc
#BSUB -W 30
#BSUB -n 20
#BSUB -R "rusage[mem=1GB]"
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -o mandelbrot-job-script_%J.out
#BSUB -e mandelbrot-job-script_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

for n_proc in 1 2 4 8 12 16 20; do
    python -u mandelbrot.py $n_proc
done
