import random

# Class creates a file of randomly generated kmers.
# Sometimes concurrency makes the program produce the wrong number
# of kmers. Just re-run the program until you get the correct amount.
class KmerGenerator:

    # Method generates a list of randomly generated kmers.
    @staticmethod
    def generateRandomKmers(numberOfKmers, kmerLength):
        randomKmers = []
        for index in range(0, numberOfKmers):
            randomKmer = KmerGenerator.__generateRandomKmer(kmerLength)
            if randomKmer in randomKmers or randomKmer[::-1] in randomKmers:
                numberOfKmers = numberOfKmers + 1
            else:
                randomKmers.append(randomKmer)
        file = open("random_kmers.fa", "a")
        for kmer in randomKmers:
            file.write(">\n" + kmer + "\n")
            file.write(">\n" + kmer[::-1] + "\n")
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