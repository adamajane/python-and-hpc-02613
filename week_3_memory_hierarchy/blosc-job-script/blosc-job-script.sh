#! /bin/bash
#BSUB -J blosc-job-script
#BSUB -q hpc
#BSUB -W 15
#BSUB -R "rusage[mem=4GB]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -n 1
#BSUB -o blosc-job-script_%J.out
#BSUB -e blosc-job-script_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

for n in 256 512 1024; do
    echo "n=$n"
    python -u blosc-job.py $n
done
