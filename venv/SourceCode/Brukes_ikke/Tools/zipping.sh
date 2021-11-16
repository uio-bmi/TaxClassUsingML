#!/usr/bin/sh
#SBATCH --account=nn9383k
#SBATCH --job-name=zipping
#SBATCH --time=0-00:10:00
#SBATCH --mem-per-cpu=16MB
#SBATCH --ntasks=1

FILES=./Counts/*
for f in $FILES
do
  gunzip $f
done


exit 0
