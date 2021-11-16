#!/usr/bin/sh
#SBATCH --account=nn9383k
#SBATCH --job-name=taxonomic_classification
#SBATCH --time=1-00:00:00
#SBATCH --mem-per-cpu=20GB

python main.py

exit 0