# This class is used to prepare the dataset for training by transforming it to a more workable format.
# This includes splitting the given FASTA file into seperate training and answer sets, as well as counting k-mers.

import numpy as np

class FastaGeneDataset:
    __trainingSet = []
    __trainingLabels = []

    def __init__(self, file, kmerLength):
        # Create list with all elements in file.
        dataset = file.read().split(">")
        dataset.pop(0)
        dataset = dataset[:5]
        for element in dataset:
            temp = element.split("\n")
            self.__trainingLabels.append(float(temp[0]))
            self.__trainingSet.append(temp[1])
        # Transform training set to appropriate format.
        self.__trainingSet = self.__prepareTrainingSet(self.__trainingSet, kmerLength)

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
    def __countKmers(kmers):
        kmer_counts = []
        unique_kmers = []

        # Add every new k-mer discovered to the output arrays.
        while len(kmers) > 0:
            elem = kmers[0]
            kmer_counts.append(1)
            unique_kmers.append(elem)

            # Look for other identical k-mers in the list, count them and delete them.
            index = 1
            temp = []
            while index < len(kmers):
                other = kmers[index]
                if elem == other:
                    kmer_counts[-1] += 1
                    del kmers[index]
                    if index > 1:
                        index -= 1
                index += 1

            # Delete the k-mer which has been added to the list so it's only counted once.
            del kmers[0]

        kmer_counts = kmer_counts[:1500]
        kmer_counts = np.array(kmer_counts, float)
        unique_kmers = np.array(unique_kmers, str)
        result = np.array([kmer_counts, unique_kmers], dtype=object)
        return result

    # Method transforms the dataset from raw data into a float vector representation for each element in
    # the training set.
    def __prepareTrainingSet(self, set, kmerLength):
        training_set = []

        for elem in set:
            kmers = self.__seqToKmers(elem, kmerLength)
            float_rep = self.__countKmers(kmers)
            training_set.append(float_rep[0])

        training_set = np.array(training_set, dtype=np.float)
        training_set = training_set / 255.0

        return training_set