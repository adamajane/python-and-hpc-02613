#! /bin/bash
#BSUB -J job-dependencies-1
#BSUB -q hpc
#BSUB -W 5
#BSUB -n 1
#BSUB -R "rusage[mem=512MB]"
#BSUB -w "done(1234567)"
#BSUB -o job-dependencies-1_%J.out
#BSUB -e job-dependencies-1_%J.err

echo "previous job 1234567 finished successfully"
