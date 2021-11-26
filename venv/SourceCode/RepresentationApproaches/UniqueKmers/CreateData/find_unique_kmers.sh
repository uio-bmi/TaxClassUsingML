#!/usr/bin/sh
#SBATCH --account=nn9383k
#SBATCH --job-name=find_unique_kmers
#SBATCH --time=1-00:00:00
#SBATCH --mem-per-cpu=1GB
#SBATCH --ntasks=1

python main.py

exit 0