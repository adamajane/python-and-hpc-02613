#! /bin/bash
#BSUB -J sleeper_2
#BSUB -q hpc
#BSUB -W 2
#BSUB -B
#BSUB -N
#BSUB -R "rusage[mem=512MB]"
#BSUB -o sleeper_%J.out
#BSUB -e sleeper_%J.err

sleep 60