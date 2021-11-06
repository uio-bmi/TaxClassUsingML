import os
import json
import sys
from label_maker import LabelMaker
import numpy as np

class SignatureTransformer:

    kmers = [] #All k-mers in set of signatures
    classifications = {} #All classification labels and corresponding file name
    classes = []  # All classes in set of signatures

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
    def __transformSignsAndLabels(self):
        for file in os.listdir("./Signatures/"):

            #Get signature
            content = open(os.path.join("./Signatures/", file)).read()[1:-1]
            content = json.loads(content)
            signature = content["signatures"][0]["mins"]
            #Create binary vector from signature
            binaryVector = self.__createBinaryVector(signature)
            self.vectors.append(binaryVector)

            #Get label
            label = content["filename"].replace("./TrainingSet/", "").replace("_genomic.fna.gz", "")
            label = self.classifications[label]
            #Create one-hot encoding vector from label
            label = LabelMaker.getOneHotEncoding(label, self.classes)
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
    def doTransformation(self, speciesLevel):
        self.__createKmerDictionary()
        self.classifications = LabelMaker.getSpeciesDictionary(speciesLevel)
        self.classes = LabelMaker.getClasses(self.classifications)
        self.__transformSignsAndLabels()

    # Method returns all binary vectors.
    def getSignatures(self):
        return self.vectors

    # Method returns all vector labels.
    def getLabels(self):
        return self.labels
