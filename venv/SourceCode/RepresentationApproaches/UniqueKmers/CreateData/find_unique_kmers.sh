#!/usr/bin/sh
#SBATCH --account=nn9383k
#SBATCH --job-name=unique_kmers
#SBATCH --time=1-00:00:00
#SBATCH --mem-per-cpu=64GB
#SBATCH --ntasks=16

python main.py

exit 0