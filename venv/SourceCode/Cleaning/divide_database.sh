#!/usr/bin/sh
#SBATCH --account=nn9383k
#SBATCH --job-name=dividing_database
#SBATCH --time=0-00:05:00
#SBATCH --mem-per-cpu=150MB

python main.py

exit 0