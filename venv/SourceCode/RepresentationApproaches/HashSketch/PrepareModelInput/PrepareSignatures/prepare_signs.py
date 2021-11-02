import os
import json
import sys
from label_maker import LabelMaker
import numpy as np

class PrepareSigns:

    kmers = [] #All k-mers in set of signatures
    species = {} #All species labels in set of signatures
    vectors = [] #All binary vectors
    labels = [] #All binary vector labels

    # Method goes through all k-mers in all_sign.fna document and adds them to
    # an array.
    def __createKmerDictionary(self):
        linesOfKmers = open("all_sign.fna", "r").readlines()
        for line in linesOfKmers:
            self.kmers.append(line)

    # Method loops through every signature file in directory and creates an array of
    # binary vectors.
    def __transformSignatures(self):
        for file in os.listdir("./Signatures/"):
            #Open signature file
            content = open(os.path.join("./Signatures/", file)).read()[1:-1]
            content = json.loads(content)
            signature = content["signatures"][0]["mins"]
            #Create binary vector from signature
            binaryVector = self.__createBinaryVector(signature)
            self.vectors.append(binaryVector)
            #Add correct classification label to corresponding species array
            label = content["filename"].replace("./TrainingSet/", "").replace("_genomic.fna.gz", "")
            label = self.species[label]
            self.labels.append(label)

    # Method takes a signature and returns its binary vector.
    def __createBinaryVector(self, signature):
        binaryVector = []
        for kmer in self.kmers:
            if int(kmer) in signature:
                 binaryVector.append(1)
            else:
                binaryVector.append(0)
        return binaryVector

    # Method transforms all signatures to binary vectors and classification
    # labels to numerical format.
    def doTransformation(self):
        self.species = LabelMaker.getSpeciesDictionary(True)
        self.__createKmerDictionary()
        self.__transformSignatures()
        self.labels = LabelMaker.transformLabels(self.labels, self.species)

    # Method returns all binary vectors.
    def getSignatures(self):
        return self.vectors

    # Method returns all vector labels.
    def getLabels(self):
        return self.labels
