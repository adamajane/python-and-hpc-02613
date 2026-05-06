#! /bin/bash
#BSUB -J sleeper_3
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=512MB]"
#BSUB -R "select[model == XeonE5_2660v3]"
#BSUB -o sleeper_%J.out
#BSUB -e sleeper_%J.err

sleep 60
