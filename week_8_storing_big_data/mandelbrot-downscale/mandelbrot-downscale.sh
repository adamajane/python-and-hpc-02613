#! /bin/bash
#BSUB -J mandelbrot-downscale
#BSUB -q hpc
#BSUB -W 5
#BSUB -n 1
#BSUB -R "rusage[mem=512MB]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -o mandelbrot-downscale_%J.out
#BSUB -e mandelbrot-downscale_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613_2026

INPUT=/dtu/projects/02613_2025/data/mandelbrot/mandelbrot.raw

for step in 1 2 4 8 16; do
    echo "step=$step"
    /usr/bin/time -f"mem=%M KB runtime=%e s" python -u mandelbrot-downscale.py "$INPUT" 4000 $step 2>&1
done
