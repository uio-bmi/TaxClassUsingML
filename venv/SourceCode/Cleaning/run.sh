#!/usr/bin/sh
#SBATCH --account=nn9383k
#SBATCH --job-name=cleaning
#SBATCH --time=0-12:00:00
#SBATCH --mem-per-cpu=1500MB

python main.py

exit 0