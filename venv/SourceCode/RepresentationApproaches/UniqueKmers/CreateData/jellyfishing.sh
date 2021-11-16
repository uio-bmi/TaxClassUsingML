#!/usr/bin/sh
#SBATCH --account=nn9383k
#SBATCH --job-name=jellyfishing
#SBATCH --time=1-00:00:00
#SBATCH --mem-per-cpu=150MB
#SBATCH --ntasks=1

module load Jellyfish/2.3.0-GCC-9.3.0

FILES=./TrainingSet/*
for f in $FILES
do
 gunzip -c $f > $f_temp.fna
 jellyfish count -m 12 -s 100M -C -t 10 -o $f.jf $f_temp.fna
 jellyfish dump $f.jf > $f.fa
 mv $f.fa ./Counts/
 mv $f ./Counted_training_set/
 rm $f.jf
done