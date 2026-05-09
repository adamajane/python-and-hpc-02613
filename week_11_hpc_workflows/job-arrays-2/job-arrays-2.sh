#! /bin/bash
#BSUB -J job-arrays-2[2,29,71,73,127]
#BSUB -q hpc
#BSUB -W 5
#BSUB -n 1
#BSUB -R "rusage[mem=512MB]"
#BSUB -R "span[hosts=1]"
#BSUB -o job-arrays-2_%J_%I.out
#BSUB -e job-arrays-2_%J_%I.err

echo "array index: $LSB_JOBINDEX"
