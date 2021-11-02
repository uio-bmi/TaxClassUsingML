import os
import json

# Class used to combine k-mer hashes from MinHash signatures to a single
# document.
class CombineSignatures:

    # Method loops over all files and finds their signature, then adds the k-mers
    # in the signature to the all_sign file.
    @staticmethod
    def loopOverSignatures():
        for file in os.listdir("./Signatures/"):
            print("Working on file " + file + "...")
            #Get signature from signature file
            content = open(os.path.join("./Signatures/", file)).read()[1:-1]
            content = json.loads(content)
            signature = content["signatures"][0]["mins"]
            #Add each k-mer in the signature to the all_sign file.
            for kmer in signature:
                CombineSignatures.__addKmer(str(kmer))
            os.rename("./Signatures/" + file, "./Finished/" + file)
            print("Finished with file " + file)

    # Method adds a k-mer hash to the all_sign file if it is not
    # already present.
    @staticmethod
    def __addKmer(kmer):
        with open("all_sign.fna", "r+") as file:
            if kmer not in file.read():
                file.write(kmer + "\n")
