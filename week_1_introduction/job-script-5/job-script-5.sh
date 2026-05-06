#! /bin/bash
#BSUB -J sleeper_5
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=512MB]"
#BSUB -n 16
#BSUB -R "span[hosts=1]"
#BSUB -o sleeper_%J.out
#BSUB -e sleeper_%J.err

sleep 60