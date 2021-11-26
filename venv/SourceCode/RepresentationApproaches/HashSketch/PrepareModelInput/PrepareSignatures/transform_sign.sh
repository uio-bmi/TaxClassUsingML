#!/bin/bash
#SBATCH --account=nn9383k
#SBATCH --job-name=transform_signatures
#SBATCH --time=1-00:00:00
#SBATCH --mem-per-cpu=1GB
#SBATCH --ntasks=1

module load Python/3.9.5-GCCcore-10.3.0
# Set the ${PS1}
export PS1=\$
source numpy_envir/bin/activate

python main.py

exit 0
