#! /bin/bash
#BSUB -J pandas-chunks
#BSUB -q hpc
#BSUB -W 30
#BSUB -n 1
#BSUB -R "rusage[mem=2GB]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -o pandas-chunks_%J.out
#BSUB -e pandas-chunks_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

INPUT=/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip

for cs in 1000 10000 100000 1000000; do
    echo "chunksize=$cs"
    /usr/bin/time -f"mem=%M KB runtime=%e s" python -u pandas-chunks.py "$INPUT" $cs 2>&1
done
