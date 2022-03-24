#!/bin/bash -l

#$ -P dl523

#$ -l gpus=1
#$ -l gpu_c=7.0

#$ -pe omp 8 
#$ -j y
#$ -o ./log.txt



module load miniconda/4.9.2
conda activate cs640
module load cuda/11.3

cd /projectnb/dl523/students/pranchan/Data-Ordering-Adversarial-Attacks

python train.py