# This class is used to prepare the dataset for training by transforming it to a more workable format.
# This includes standardizing the DNA sequences for more convenient comparison.

import numpy as np
from Tools.dictionary import Dictionary
from Tools.set_manipulation import SetManupulation

class FastaGeneDataset:
    __trainingSet = []
    __trainingLabels = []

    def __init__(self, file, kmerLength):
        # Create list with all elements in file.
        dataset = file.read().split(">")
        dataset.pop(0)
        dataset = dataset[:100]

        # Initialize dictionaries
        kmerDictionary = Dictionary(True) # To hold all kmers
        labelDictionary = Dictionary(False) # To hold all labels

        for elem in dataset:
            temp = elem.split("\n")

            # Add element to training set and label set
            self.__trainingLabels.append(float(temp[0]))
            self.__trainingSet.append(self.__seqToKmers(temp[1], kmerLength))

            # Add values to dictionaries
            kmers = self.__seqToKmers(temp[1], kmerLength)
            kmerDictionary.addSetToCounterDictionary(kmers)
            labelDictionary.addToIndexDictionary(float(temp[0]))

        # Remove common kmers from dictionary
        kmerDictionary.counterDictionaryCommonalityThresholdRemoval(50)
        kmerDictionary.addSetToDictionary(kmerDictionary.getCounterDictionary())

        # Format training and label sets.
        self.__trainingSet = self.__prepareTrainingSet(self.__trainingSet, kmerDictionary.getIndexDictionary())
        self.__trainingLabels = self.__prepareLabelSet(self.__trainingLabels, labelDictionary.getIndexDictionary())


    # Method returns all training sequences.
    def getTrainingSet(self):
        return self.__trainingSet

    # Method returns the training labels for the dataset.
    def getTrainingLabels(self):
        return self.__trainingLabels

    # Method returns a specific element from the training set.
    def getTrainingElement(self, index):
        return self.__trainingSet[index]

    # Method returns a specific answer from the label set.
    def getTrainingLabel(self, index):
        return self.__trainingLabels[index]

    # Method transforms a DNA sequence into list of k-mers of given length.
    @staticmethod
    def __seqToKmers(sequence, kmer_length):
        nuc_sequence = sequence
        kmer_sequence = []
        for nuc in range(len(nuc_sequence) - kmer_length):
            temp = ""
            for element in range(kmer_length):
                temp += nuc_sequence[nuc + element]
            kmer_sequence.append(temp)
        return kmer_sequence

    # Method transforms the training set replacing each element with a numerical representation.
    def __prepareTrainingSet(self, set, kmerDictionary):
        training_set = []
        seqLength = SetManupulation.findLongestList(set)
        for elem in set: #Go through each sequence
            temp = [0] * seqLength
            for index in range(seqLength - 1): # Go through each kmer in sequence
                try: #Replace kmer with number from dictionary
                    kmer_num = kmerDictionary.get(elem[index])
                    if kmer_num != None:
                       temp[index] = kmer_num
                    else:
                       temp[index] = 0
                except:
                    temp[index] = 0
            training_set.append(temp)
        training_set = np.array(training_set, dtype=np.float)
        training_set = training_set / 255.0
        return training_set

    # Method takes a set of labels and returns a numpy array where each label has
    # been encoded.
    def __prepareLabelSet(self, trainingLabels, labelDictionary):
        labels = []
        for label in trainingLabels:
            temp = labelDictionary[label]
            labels.append(temp)
        labels = np.array(labels, dtype=np.float)
        return labels
