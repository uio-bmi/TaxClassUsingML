import numpy as np
import sourmash
from sourmash import fig
import csv
import pandas as pd

# This class fetches signatures created using MinHash.
class MinHashInput:

   # Method retrieves the MinHash singnatures from a document. These singatures have already
   # been transformed to a comparable format.
   @staticmethod
   def getTrainingSet():
       print("Preparing MinHash training set...")
       speciesNames = MinHashInput.__readSpeciesNames()
       matrix, labels = fig.load_matrix_and_labels("./compare-demo")

       #Transform label names to species names.
       for index, label in enumerate(labels):
           species = speciesNames.get(label.replace("./Database/", "").replace("_genomic.fna.gz", ""))
           labels[index] = species

       #Replace species names with numerical representation.
       speciesDictionary = {}
       speciesDictionary["Unknown"] = 0
       for index, species in enumerate(labels):
           if species in speciesDictionary:
               labels[index] = speciesDictionary[species]
           else:
               labels[index] = len(speciesDictionary)
               speciesDictionary[species] = len(speciesDictionary)
       labels = np.array(labels, dtype=float)
       labels = labels / 255.0

       print("Saving to csv")
       pd.DataFrame(matrix).to_csv("./data.csv", header=None, index=None)
       pd.DataFrame(labels).to_csv("./data_labels.csv", header=None, index=None)
       print("Finished preparing MinHash dataset")


   # Method reads the species label for each file in the database and transfers
   # those to a set which is then returned.
   @staticmethod
   def __readSpeciesNames():
       labels = {}
       labels_file = open("./gtdb_taxonomy.tsv", encoding="utf8")
       label_reader = csv.reader(labels_file, delimiter="\t", quotechar='"')
       for row in label_reader:
           labels[row[0].replace("GB_", "").replace("RS_", "")] = row[1]
       return labels

