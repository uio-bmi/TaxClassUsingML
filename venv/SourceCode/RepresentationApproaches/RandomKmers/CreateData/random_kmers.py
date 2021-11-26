import random

# Class creates a file of randomly generated k-mers.
class KmerGenerator:

    # Method generates a list of randomly generated kmers.
    @staticmethod
    def generateRandomKmers(numberOfKmers, kmerLength):
        randomKmers = []
        while len(randomKmers) < numberOfKmers:
            randomKmer = KmerGenerator.__generateRandomKmer(kmerLength)
            if randomKmer not in randomKmers or randomKmer[::-1] not in randomKmers:
                randomKmers.append(randomKmer)
        file = open("random_kmers.fa", "a")
        for kmer in randomKmers:
            file.write(">\n" + kmer + "\n")
        file.close()
        return randomKmers

    # Method generates a random k-mer of given length.
    @staticmethod
    def __generateRandomKmer(kmerLength):
        randomKmer = ""
        nucleotides = ["A", "C", "T", "G"]
        for index in range(0, kmerLength):
            randomNucleotide = nucleotides[random.randint(0, 3)]
            randomKmer = randomKmer + randomNucleotide
        return randomKmer