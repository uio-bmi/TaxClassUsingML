import os
import gzip

class UniqueKmerSelector:
    unique_kmers = {}
    useless_kmers = {}

    # Method adds a kmer to the class dictionaries.
    def __addToDictionary(self, kmer):
        if kmer in self.unique_kmers or kmer[::-1] in self.unique_kmers:
            del self.unique_kmers[kmer]
            self.useless_kmers[kmer] = 1
        else:
            self.unique_kmers[kmer] = 1

    # Method finds all unique kmers in a folder of kmer counts.
    def getUniqueKmers(self):
        print("Finding unique kmers...")
        path = "./Counts/"
        for file in os.listdir(path):
            fullpath = os.path.join(path, file)
            with gzip.open(fullpath, "rt") as f:
                for line in f:
                    if line.find(">"):
                        self.__addToDictionary(line)
        print("Finished finding unique kmers")
        return self.unique_kmers

    # Method takes an array of kmers and writes them to a file.
    @staticmethod
    def writeKmersToFile(kmers):
        print("Writing kmers to file...")
        file = open("./unique_kmers.fa", "w")
        for kmer in kmers:
            file.write(">\n" + kmer)
        file.close()
        print("Finished writing kmers to file")
