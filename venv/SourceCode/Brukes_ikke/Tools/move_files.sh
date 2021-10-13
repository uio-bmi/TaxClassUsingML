#!/bin/bash

DIRECTORIES=./GCF/*
for d in $DIRECTORIES
do
 FOLDERS=$d/*
 for f in $FOLDERS
 do
   FILES=$f/*
   for i in $FILES
   do
     mv $i ./904/
   done
 done
done
