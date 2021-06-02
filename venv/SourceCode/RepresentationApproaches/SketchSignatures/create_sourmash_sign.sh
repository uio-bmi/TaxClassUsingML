#!/bin/bash
FILES=./Database/*
for f in $FILES
do
  sourmash sketch dna -p num=5000,k=31 $f -o $f.sig
  mv $f.sig ./Signatures/
done