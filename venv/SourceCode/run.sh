#!/usr/bin/sh
#SBATCH --account=nn9383k
#SBATCH --job-name=taxonomic_classification
#SBATCH --time=0-00:10:00
#SBATCH --mem-per-cpu=1500MB

python main.py

exit 0