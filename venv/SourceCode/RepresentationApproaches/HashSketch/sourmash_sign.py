import os
import json
import numpy as np
import csv

# Class prepares data input based on Sourmash sketches.
class HashSketches:

    # Method creates a dictionary with all the file names and corresponding species labels
    # from the gtdb_taxonomy.tsv file.
    @staticmethod
    def __getFileSpeciesDictionary():
        labels = {}
        labels_file = open("./RepresentationApproaches/HashSketch/gtdb_taxonomy.tsv", encoding="utf8")
        label_reader = csv.reader(labels_file, delimiter="\t", quotechar='"')
        for row in label_reader:
            genusLabel = row[1].split(";g__", 1)[0]
            labels[row[0].replace("GB_", "").replace("RS_", "")] = genusLabel
        return labels

    # Method returns the hash sketches and species labels.
    @staticmethod
    def __getRawHashSignAndSpeciesLables():
        path = "./RepresentationApproaches/HashSketch/Signatures/"
        signatures = []
        speciesNames = HashSketches.__getFileSpeciesDictionary()
        labels = []
        for file in os.listdir(path):
            content = open(os.path.join(path, file)).read()[1:-1]
            content = json.loads(content)
            signature = content["signatures"][0]["mins"]
            signatures.append(signature)
            labels.append(speciesNames[file.replace("_genomic.fna.gz.sig", "")])
        return [signatures, labels]

    @staticmethod
    def __transformToNumerical(signatures, labels):
        #Transform signatures
        signatures = np.array(signatures, dtype=float)
        signatures = signatures / 255.0

        #Transform labels
        speciesDictionary = {}
        for index, species in enumerate(labels):
            if species in speciesDictionary:
                labels[index] = speciesDictionary[species]
            else:
                labels[index] = len(speciesDictionary)
                speciesDictionary[species] = len(speciesDictionary)
        print("her", len(speciesDictionary))
        labels = np.array(labels, dtype=float)
        labels = labels / 255.0
        return [signatures, labels]

    # Method returns data input ready for use in models.
    @staticmethod
    def getData():
        rawData = HashSketches.__getRawHashSignAndSpeciesLables()
        numericalData = HashSketches.__transformToNumerical(rawData[0], rawData[1])
        return numericalData
