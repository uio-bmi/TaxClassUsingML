#!/usr/bin/sh
#SBATCH --account=nn9383k
#SBATCH --job-name=unique kmers
#SBATCH --time=1-00:00:00
#SBATCH --mem-per-cpu=32GB
#SBATCH --ntasks=8

python main.py

exit 0