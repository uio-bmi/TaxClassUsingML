import os
from label_maker import LabelMaker

# Class used to transform files of k-mer counts to list of usable input vectors.
class CountTransformer:

    vectors = []
    labels = []

    # Method transforms the files from the Counts directory to vector representations
    # and finds the correct classification for each file.
    def doTransformation(self, speciesLevel, countBased):
        classifications = LabelMaker.getSpeciesDictionary(speciesLevel)
        classes = LabelMaker.getClasses(classifications) #All classes in set of files
        for file in os.listdir("Counts"):
            #Create vector representation
            self.vectors.append(self.__getVectorRepresentation(file, countBased))
            #Create classification label
            classification = classifications[file.replace("_genomic.fna.gz.fa.gz", "")]
            classification = LabelMaker.getOneHotEncoding(classification, classes)
            self.labels.append(classification)

    # Method transforms a k-mer count file to a vector representation of counts.
    def __getVectorRepresentation(self, kmerFile, countBased):
        counts = open(os.path.join("./Counts/", kmerFile)).readlines()
        vector = []
        for line in counts:
            if ">" in line:
                vector.append(int(line.replace(">", "").replace("\n", "")))
        if countBased:
            vector = self.__scaleCountVector(vector)
        else:
            vector = self.__scalePresenceVector(vector)
        return vector

    # Method scales a k-mer count vector so that all values are between 0 and 1.
    def __scaleCountVector(self, vector):
        scaled_vector = []
        max_value = max(vector)
        min_value = min(vector)
        for value in vector:
            scaled_value = (value - min_value)/(max_value - min_value)
            scaled_vector.append(scaled_value)
        return scaled_vector

    # Method takes k-mer count vector and returns a binary vector denoting only
    # presence/absence.
    def __scalePresenceVector(self, vector):
        binary_vector = []
        for value in vector:
            if value > 0:
                binary_vector.append(1)
            else:
                binary_vector.append(0)
        return binary_vector

    # Method returns list of representation vectors.
    def getVectors(self):
        return self.vectors

    # Method returns list of classification labels.
    def getLabels(self):
        return self.labels