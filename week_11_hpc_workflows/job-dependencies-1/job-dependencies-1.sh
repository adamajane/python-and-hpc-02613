#! /bin/bash
#BSUB -J job-dependencies-1
#BSUB -q hpc
#BSUB -W 5
#BSUB -n 1
#BSUB -R "rusage[mem=512MB]"
#BSUB -R "select[model == XeonE5_2660v3]"
#BSUB -o job-dependencies-1_%J.out
#BSUB -e job-dependencies-1_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026
