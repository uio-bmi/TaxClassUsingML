#!/usr/bin/sh
#SBATCH --account=TaxonomicClassification
#SBATCH --job-name=taconomic_classification
#SBATCH --partition=optimist
#SBATCH --NODES=1
#SBATCH --time=0-00:05:00
#SBATCH --mem-per-cpu=1500MB

python main.py

exit 0