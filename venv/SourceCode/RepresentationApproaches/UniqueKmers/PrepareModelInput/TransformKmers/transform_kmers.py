import os
from label_maker import LabelMaker

# Class used to transform files of discriminative k-mers to list of usable input vectors.
class DiscriminativeTransformer:

    kmers = []  # All k-mers in set
    classifications = {}  # All classification labels and corresponding file names
    classes = []  # All classes in set

    vectors = []  # All binary vectors
    labels = []  # All binary vector labels

    # Method goes through all k-mers in document and adds them to
    # an array.
    def __createKmerDictionary(self):
        linesOfKmers = open("all_kmers.fna", "r").readlines()
        for line in linesOfKmers:
            self.kmers.append(line)

    # Method loops through every file in directory and creates an array of
    # binary vectors.
    def __transformSignsAndLabels(self):
        for file in os.listdir("./Counts/"):
            # Get k-mer
            kmer = open(os.path.join("./Counts/", file)).read()[1]
            # Create binary vector
            binaryVector = self.__createBinaryVector(kmer)
            self.vectors.append(binaryVector)
            # Get label
            label = content["filename"].replace("./Counts/", "").replace("_genomic.fna.gz", "")
            label = self.classifications[label]
            # Create one-hot encoding vector from label
            label = LabelMaker.getOneHotEncoding(label, self.classes)
            self.labels.append(label)

    # Method takes a k-mer and returns a binary vector over all k-mers.
    def __createBinaryVector(self, discKmer):
        binaryVector = []
        for kmer in self.kmers:
            if kmer is discKmer:
                binaryVector.append(1)
            else:
                binaryVector.append(0)
        return binaryVector

    # Method transforms all discriminative k-mers to binary vectors and classification
    #labels to numerical format.
    def doTransformation(self, speciesLevel):
        self.__createKmerDictionary()
        self.classifications = LabelMaker.getSpeciesDictionary(speciesLevel)
        self.classes = LabelMaker.getClasses(self.classifications)
        self.__transformSignsAndLabels()

    # Method returns all binary vectors.
    def getVectors(self):
        return self.vectors

    # Method returns all vector labels.
    def getLabels(self):
        return self.labels