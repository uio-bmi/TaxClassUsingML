#!/bin/bash
#SBATCH --account=nn9383k
#SBATCH --job-name=jellyfishing
#SBATCH --time=1-00:00:00
#SBATCH --mem-per-cpu=50MB
#SBATCH --ntasks=1

module load Jellyfish/2.3.0-GCC-9.3.0

FILES=./TrainingSet/*
for f in $FILES
do
 zcat $f > $f_temp.fna
 jellyfish count -m 12 -s 100M -C -t 10 -o $f.jf --if random_kmers.fa $f_temp.fna
 rm $f_temp.fna
 jellyfish dump $f.jf > $f.fa
 rm $f.jf
 gzip $f.fa
 mv $f.fa.gz ./Counts/
 rm $f
done

exit 0

