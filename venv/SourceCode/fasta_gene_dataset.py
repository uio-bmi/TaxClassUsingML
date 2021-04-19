# This class is used to prepare the dataset for training by transforming it to a more workable format.
# This includes standardizing the DNA sequences for more convenient comparison.
import math
import random

import numpy as np
from Tools.dictionary import Dictionary
from Tools.set_manipulation import SetManupulation
from PreProcessing.data_reader import DataReader
from PreProcessing.generate_test_set import GenerateTestSet
import os
import gzip

class FastaGeneDataset:
    __trainingSet = []
    __trainingLabels = []
    __testSet = []
    __testLabels = []
    __totalCountKmers = 0

    def __init__(self, kmerLength):

        # Read database
        data = DataReader.readDataFiles()
        filenames = data[0] #Array with all filenames
        seq = data[1] #Set with format: { filename: { DNA scaffolds } }
        species_labels = DataReader.readSpeciesNames() #Set with format: { filename: species }

        # Initialize dictionaries
        kmerDictionary = Dictionary(True)  # To hold all kmers
        speciesDictionary = Dictionary(False)  # To hold all labels
        for species in species_labels:
            speciesDictionary.addToIndexDictionary(species_labels[species])

        for filename in filenames:
            for scaffold in seq[filename]:
              #Cut kmers
              arr_of_kmers = self.__seqToKmers(scaffold, kmerLength)

              #Add data to training sets
              self.__trainingLabels.append(species_labels[filename])
              self.__trainingSet.append(arr_of_kmers)

              kmerDictionary.addSetToCounterDictionary(arr_of_kmers)

        # Remove common kmers from index dictionary
        kmerDictionary.counterDictionaryCommonalityThresholdRemoval(75)
        kmerDictionary.addSetToDictionary(kmerDictionary.getCounterDictionary())
        self.__totalCountKmers = kmerDictionary.len()

        # Divide training set into training and test sets
        temp = GenerateTestSet.getDividedSets(self.__trainingSet, self.__trainingLabels)
        self.__testSet = temp[0]
        self.__testLabels = temp[1]
        self.__trainingSet = temp[2]
        self.__trainingLabels = temp[3]

        # Format training and label sets.
        print("Re-formatting training and test set...")
        seqLength = SetManupulation.findLongestList(self.__trainingSet)
        self.__trainingSet = self.__prepareTrainingSet(self.__trainingSet, kmerDictionary.getIndexDictionary(), seqLength)
        self.__trainingLabels = self.__prepareLabelSet(self.__trainingLabels, speciesDictionary.getIndexDictionary())
        self.__testSet = self.__prepareTrainingSet(self.__testSet, kmerDictionary.getIndexDictionary(), seqLength)
        self.__testLabels = self.__prepareLabelSet(self.__testLabels, speciesDictionary.getIndexDictionary())
        print("Finished formating training and test set")


    # Method returns the total number of kmers.
    def getTotalCountKmers(self):
        return self.__totalCountKmers

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

    # Method returns the test set for the dataset.
    def getTestSet(self):
        return self.__testSet

    # Method returns the test labels for the dataset.
    def getTestLabels(self):
        return self.__testLabels


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
    def __prepareTrainingSet(self, set, kmerDictionary, seqLength):
        training_set = []
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
        return training_set

    # Method takes a set of labels and returns a numpy array where each label has
    # been encoded.
    def __prepareLabelSet(self, trainingLabels, labelDictionary):
        labels = []
        for label in trainingLabels:
            labels.append(labelDictionary[label])
        labels = np.array(labels, dtype=np.float)
        return labels
