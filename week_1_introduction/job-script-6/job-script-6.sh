#! /bin/bash
#BSUB -J sleeper_6
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=512MB]"
#BSUB -n 64
#BSUB -R "span[hosts=1]"
#BSUB -o sleeper_%J.out
#BSUB -e sleeper_%J.err

sleep 60