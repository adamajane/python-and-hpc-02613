#! /bin/bash
#BSUB -J job-arrays-1[1-10]
#BSUB -q hpc
#BSUB -W 5
#BSUB -n 1
#BSUB -R "rusage[mem=512MB]"
#BSUB -R "span[hosts=1]"
#BSUB -o job-arrays-1_%J_%I.out
#BSUB -e job-arrays-1_%J_%I.err

echo "array index: $LSB_JOBINDEX"
