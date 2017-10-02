#!/bin/bash

#SBATCH --job-name=parallelJob
#SBATCH --output=parallelJob_%j.out
#SBATCH --error=parallelJob_%j.err
#SBATCH --time=08:00:00
#SBATCH --partition=broadwl
#SBATCH --ntasks=100


######################
# Begin work section #
######################

module load parallel
module load ffmpeg

echo "Job started at `date`"

#input_list.txt has the name of all files to be processed
lines=$(wc -l input_list.txt)

srun="srun -n 1 -N 1 --exclusive"
parallel="parallel --delay .2 -j $SLURM_NTASKS --joblog runtask.log --resume" 

$parallel "$srun ./run_task_generic.sh {1}" ::: `seq 1 $lines`

echo "Job finished at `date`"

