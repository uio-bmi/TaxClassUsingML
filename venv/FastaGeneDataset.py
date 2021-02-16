# This class is used to prepare the dataset for training by transforming it to a more workable format.
# This includes splitting the given FASTA file into seperate training and answer sets, as well as counting k-mers.

class FastaGeneDataset:
    __dataset = []
    __trainingSet = []
    __answers = []

    def __init__(self, file):
        # Create list with all elements in file.
        self.__dataset = file.read().split(">")
        self.__dataset.pop(0)
        for element in self.__dataset:
            temp = element.split("\n")
            self.__answers.append(temp[0])
            self.__trainingSet.append(temp[1])

    # Method returns all training sequences.
    def getTrainingSet(self):
        return self.__trainingSet

    # Method returns all correct classification for each sequence.
    def getAnswers(self):
        return self.__answers

    # Method returns a specific element from the training set.
    def getTrainingElement(self, index):
        return self.__trainingSet[index]

    # Method returns a specific answer from the answer set.
    def getAnswer(self, index):
        return self.__answers[index]

    # Method transforms a nucleotide sequence into list of k-mers of given length.
    @staticmethod
    def seqToKmers(sequence, kmer_length):
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
    def countKmers(kmers):
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
                    index = 0
                index += 1

            # Delete the k-mer which has been added to the list so it's only counted once.
            del kmers[0]

        return [kmer_counts, unique_kmers]