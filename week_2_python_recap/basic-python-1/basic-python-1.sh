#! /bin/bash
#BSUB -J python_1
#BSUB -q hpc
#BSUB -W 2
#BSUB -B
#BSUB -N
#BSUB -R "rusage[mem=512MB]"
#BSUB -o python_%J.out
#BSUB -e python_%J.err

# Initialize Python environment
source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

# Python script
python -u listsum.py