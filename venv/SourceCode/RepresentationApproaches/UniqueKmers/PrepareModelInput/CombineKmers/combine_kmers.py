import os
import json

# Class used to combine k-mer hashes from MinHash signatures to a single
# document.
class CombineKmers:

    # Method loops over all files and finds their signature, then adds the k-mers
    # in the signature to the all_sign file.
    @staticmethod
    def loopOverFiles():
        for file in os.listdir("./Counts/"):
            print("Working on file " + file + "...")
            #Get k-mers from file
            content = open(os.path.join("./Counts/", file)).read()[1:-1]
            content = json.loads(content)
            #Add each k-mer in the signature to the all_sign file.
            for kmer in content:
                CombineKmers.__addKmer(str(kmer))
            os.rename("./Counts/" + file, "./Finished/" + file)
            print("Finished with file " + file)

    # Method adds a k-mer hash to the all_sign file if it is not
    # already present.
    @staticmethod
    def __addKmer(kmer):
        with open("all_kmers.fna", "r+") as file:
            if kmer not in file.read():
                file.write(kmer + "\n")
