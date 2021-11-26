#!/usr/bin/sh
#SBATCH --account=nn9383k
#SBATCH --job-name=taxonomic_classification
#SBATCH --time=0-00:00:00
#SBATCH --mem-per-cpu=0GB

python main.py

exit 0