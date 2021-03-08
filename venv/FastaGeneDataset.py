# This class is used to prepare the dataset for training by transforming it to a more workable format.
# This includes standardizing the DNA sequences for more convenient comparison.

import numpy as np

class FastaGeneDataset:
    __trainingSet = []
    __trainingLabels = []

    # Contains overview of all k-mers in the dataset.
    __dictionary = {}
    __preDict = {}

    def __init__(self, file, kmerLength):
        # Create list with all elements in file.
        dataset = file.read().split(">")
        dataset.pop(0)
        dataset = dataset[:100]
        for elem in dataset:
            temp = elem.split("\n")
            # Create training set and labels.
            self.__trainingLabels.append(float(temp[0]))
            self.__trainingSet.append(self.__seqToKmers(temp[1], kmerLength))
            # Build preliminary dictionary with all kmers.
            kmers = self.__seqToKmers(temp[1], kmerLength)
            self.__preDictionary(kmers)
        self.__buildDictionary() # With fewer kmers
        self.__trainingSet = self.__prepareTrainingSet(self.__trainingSet, 1500) # With numeric values


    # Method returns all training sequences.
    def getTrainingSet(self):
        return self.__trainingSet

    # Method returns all correct classification for each sequence.
    def getTrainingLabels(self):
        return self.__trainingLabels

    # Method returns a specific element from the training set.
    def getTrainingElement(self, index):
        return self.__trainingSet[index]

    # Method returns a specific answer from the answer set.
    def getTrainingLabel(self, index):
        return self.__trainingLabels[index]


    # Method transforms a nucleotide sequence into list of k-mers of given length.
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

    # Method creates two matching arrays, one with every unique k-mer, and another with values indicating the number
    # of each k-mer.
    @staticmethod
    def __uniqueKmers(kmers):
        unique_kmers = []
        # Add every new k-mer discovered to the output arrays.
        while len(kmers) > 0:
            elem = kmers[0]
            unique_kmers.append(elem)
            # Look for other identical k-mers in the list, count them and delete them.
            index = 1
            while index < len(kmers):
                other = kmers[index]
                if elem == other:
                    del kmers[index]
                    if index > 1:
                        index -= 1
                index += 1
            # Delete the k-mer which has been added to the list so it's only counted once.
            del kmers[0]
        return unique_kmers

    # Method transforms each element in dataset from a set of kmers, to an array with a numerical
    # representation of each kmer.
    def __prepareTrainingSet(self, set):
        training_set = []
        seqLength = self.__findLongestList(set)
        for elem in set: #Go through each sequence
            temp = [0] * seqLength
            for index in range(seqLength - 1): # Go through each kmer in sequence
                try: #Replace kmer with number from dictionary
                    kmer_num = self.__dictionary.get(elem[index])
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

    # Method takes a list of lists and returns the length of the longest list.
    def __findLongestList(self, lists):
        longestLength = 0
        for list in lists:
            if len(list) > longestLength:
                longestLength = len(list)
        return longestLength


    # METHODS USED TO CREATE K-MER DICTIONARY

    # Method creates the preliminary dictionary given a set of kmers.
    def __preDictionary(self, kmers):
        for kmer in kmers:
            if self.__preDict:
                if kmer in self.__preDict.keys():
                    self.__preDict[kmer] += 1
                else:
                    self.__preDict[kmer] = 1
            else:
                self.__preDict[kmer] = 1

    # Method handles creating the final dictionary.
    def __buildDictionary(self):
        self.__weedOutUselessKmers(50)
        self.__addToDictionary()

    # Method adds kmers to the final dictionary from hte preliminary dictionary.
    def __addToDictionary(self):
        # Index 0 is reserved for un-recognisable kmers.
        index = 1
        for kmer in self.__preDict.keys():
            self.__dictionary[kmer] = index
            index += 1

    # Method removes kmers which are very common accross DNA sequences.
    def __weedOutUselessKmers(self, commonalityTreshold):
        toBeDeleted = []
        for kmer in self.__preDict.keys():
            if self.__preDict.get(kmer) > commonalityTreshold:
                toBeDeleted.append(kmer)
        for elem in toBeDeleted:
            del self.__preDict[elem]