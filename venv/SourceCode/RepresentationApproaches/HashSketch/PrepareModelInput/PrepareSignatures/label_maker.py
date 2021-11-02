import csv
import numpy as np

# Class used to create useful classification labels based on filenames and the gtdb_taxonomy.tsv file.
class LabelMaker:

    # Method creates a dictionary with all the file names and corresponding species labels
    # from the gtdb_taxonomy.tsv file.
    @staticmethod
    def getSpeciesDictionary(useSpecies):
        if useSpecies:
            splitString = ";s__"
        else:
            splitString = ";g__"
        labels = {}
        labels_file = open("../gtdb_taxonomy.tsv", encoding="utf8")
        label_reader = csv.reader(labels_file, delimiter="\t", quotechar='"')
        for row in label_reader:
            genusLabel = row[1].split(splitString, 1)[0]
            labels[row[0].replace("GB_", "").replace("RS_", "")] = genusLabel
        return labels

    # Method replaces classification labels with numerical representation.
    @staticmethod
    def transformLabels(labels, species):
        speciesDictionary = {}
        for index, label in enumerate(labels):
            if label in speciesDictionary:
                labels[index] = speciesDictionary[label]
            else:
                labels[index] = len(speciesDictionary)
                speciesDictionary[label] = len(speciesDictionary)
        labels = np.array(labels, dtype=float)
        labels = labels / np.linalg.norm(labels)
        return labels