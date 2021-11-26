#!/usr/bin/sh
#SBATCH --account=nn9383k
#SBATCH --job-name=create_sourmash_signatures
#SBATCH --time=1-00:00:00
#SBATCH --mem-per-cpu=1GB
#SBATCH --ntasks=1

module load Python/3.9.5-GCCcore-10.3.0
export PS1=\$
source smash_envir/bin/activate
conda activate smash

FILES=./TrainingSet/*
for f in $FILES
do
  sourmash sketch dna -p num=3000,k=12 $f -o $f.sig
  mv $f.sig ./Signatures/
  mv $f ./Smashed_test_set/
done