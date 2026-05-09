#! /bin/bash
#BSUB -J job-dependencies-2
#BSUB -q hpc
#BSUB -W 5
#BSUB -n 1
#BSUB -R "rusage[mem=512MB]"
#BSUB -R "span[hosts=1]"
#BSUB -w "ended(21241475)"
#BSUB -o job-dependencies-2_%J.out
#BSUB -e job-dependencies-2_%J.err

echo "all array elements of job 21241475 have ended"
