import csv
import numpy as np

# Class used to create classification labels based on filenames and the gtdb_taxonomy.tsv file.
# gtdb_taxonomy.tsv must be in the same folder as this class.
class LabelMaker:

    # Method creates a dictionary with all the file names and corresponding species labels
    # from the gtdb_taxonomy.tsv file.
    @staticmethod
    def getSpeciesDictionary(useSpecies):
        labels = {}
        labels_file = open("gtdb_taxonomy.tsv", encoding="utf8")
        label_reader = csv.reader(labels_file, delimiter="\t", quotechar='"')
        for row in label_reader:
            if useSpecies:
                label = row[1]
            else:
                label = row[1].split(";s__", 1)[0]
            labels[row[0].replace("GB_", "").replace("RS_", "")] = label
        return labels

    # Method takes a label and list of all classes and returns a one-hot-encoding
    # vector of the label.
    @staticmethod
    def getOneHotEncoding(label, classes):
        vector = []
        for elem in classes:
            if label == elem:
                vector.append(1)
            else:
                vector.append(0)
        return vector

    # Method takes in all classification labels and return a list
    # of all classes.
    @staticmethod
    def getClasses(labels):
        species = []
        for label in labels:
            if labels[label] not in species:
                species.append(labels[label])
        return species
