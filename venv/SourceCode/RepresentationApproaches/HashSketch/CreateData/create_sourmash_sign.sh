#!/usr/bin/sh
#SBATCH --account=nn9383k
#SBATCH --job-name=sourmash_signatures
#SBATCH --time=1-12:00:00
#SBATCH --mem-per-cpu=1GB
#SBATCH --ntasks=1

module load Python/3.9.5-GCCcore-10.3.0
export PS1=\$
source smash_envir/bin/activate
conda activate smash

FILES=./TrainingSet/*
for f in $FILES
do
  sourmash sketch dna -p num=5000,k=12 $f -o $f.sig
  mv $f.sig ./Signatures/
  mv $f ./Smashed_training_set/
done