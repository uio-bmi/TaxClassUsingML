#!/usr/bin/sh
#SBATCH --account=nn9383k
#SBATCH --job-name=combine_signatures
#SBATCH --time=1-00:00:00
#SBATCH --mem-per-cpu=1GB
#SBATCH --ntasks=1

module load Python/3.9.5-GCCcore-10.3.0
export PS1=\$

python main.py

exit 0