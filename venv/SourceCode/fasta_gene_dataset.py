# This class is used to prepare the dataset for training by transforming it to a more workable format.
# This includes standardizing the DNA sequences for more convenient comparison.

import numpy as np
from Tools.dictionary import Dictionary
from Tools.set_manipulation import SetManupulation
from PreProcessing.label_finder import LabelFinder
from PreProcessing.data_reader import DataReader
import os
import gzip


class FastaGeneDataset:
    __trainingSet = []
    __trainingLabels = []

    def __init__(self, kmerLength):

        # Read database
        data = DataReader.readDatabase()
        labels = data[0] #All species labels
        seq = data[1] #All DNA sequences

        # Initialize dictionaries
        kmerDictionary = Dictionary(True)  # To hold all kmers
        labelDictionary = Dictionary(False)  # To hold all labels

        for label in labels:
            for scaffold in seq[label]:
             # Cut kmers
             kmers = self.__seqToKmers(scaffold, kmerLength)

             # Add lables and sequences to training data and overview dictionaries
             self.__trainingLabels.append(label)
             self.__trainingSet.append(kmers)
             kmerDictionary.addSetToCounterDictionary(kmers)
             labelDictionary.addToIndexDictionary(label)

        # Remove common kmers from index dictionary
        kmerDictionary.counterDictionaryCommonalityThresholdRemoval(75)
        kmerDictionary.addSetToDictionary(kmerDictionary.getCounterDictionary())

        # Format training and label sets.
        self.__trainingSet = self.__prepareTrainingSet(self.__trainingSet, kmerDictionary.getIndexDictionary())
        self.__trainingLabels = self.__prepareLabelSet(self.__trainingLabels, labelDictionary.getIndexDictionary())
        print(len(self.__trainingLabels))
        print(len(self.__trainingSet))



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


    # Method transforms a DNA sequence into an array of k-mers of given length.
    @staticmethod
    def __seqToKmers(sequence, kmer_length):
        nuc_sequence = sequence
        kmer_sequences = []
        for nuc in range(len(nuc_sequence) - kmer_length):
            temp = ""
            for element in range(kmer_length):
                temp += nuc_sequence[nuc + element]
            if "N" not in temp:
               kmer_sequences.append(temp)
        return kmer_sequences

    # Method transforms the training set replacing each element with a numerical representation.
    def __prepareTrainingSet(self, set, kmerDictionary):
        print("Re-formatting training set...")
        training_set = []
        seqLength = SetManupulation.findLongestList(set)
        for elem in set: #Go through each sequence
            temp = [0] * seqLength
            for index in range(seqLength - 1): # Go through each kmer in sequence
                kmer_num = 0
                try:
                    kmer_num = kmerDictionary.get(elem[index])
                    if kmer_num == None:
                        kmer_num = kmerDictionary.get(elem[index][::-1])
                    if kmer_num != None:
                        temp[index] = kmer_num
                    else:
                        temp[index] = 0
                except:
                    temp[index] = 0
            training_set.append(temp)
        training_set = np.array(training_set, dtype=np.float)
        training_set = training_set / 255.0
        print("Finished re-formatting training set")
        return training_set

    # Method takes a set of labels and returns a numpy array where each label has
    # been encoded.
    def __prepareLabelSet(self, trainingLabels, labelDictionary):
        print("Re-formatting training labels...")
        labels = []
        for label in trainingLabels:
            labels.append(labelDictionary[label])
        labels = np.array(labels, dtype=np.float)
        print("Finished re-formatting training labels")
        return labels
