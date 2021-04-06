#!/usr/bin/sh
#SBATCH --job-name=taconomic_classification
#SBATCH --NODES=1
#SBATCH --time=0-00:01:00
#SBATCH --mem-per-cpu=1500MB

python main.py

exit 0