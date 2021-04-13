import os
import gzip

class DataReader:

    # Method reads the database and returns an array of all lables and a set of all
    # DNA sequences in the database.
    @staticmethod
    def readDatabase():
        #Open each database file
        print("Reading database...")
        path = "../Data/database/"
        labels = []
        all_nuc_sequences = {}
        #For each file in the database
        for file in os.listdir(path):
            fullpath = os.path.join(path, file)
            label = "GB_" + file.replace("_genomic.fna.gz", "")
            labels.append(label)
            nuc_sequences = {}

            #Read file
            try:
             unzipped = gzip.open(fullpath, "rt")
             contents = unzipped.readline()
             scaffold_name = ""
             #Go through each line in file
             while contents != "":
                 if ">" in contents: #Line is a scaffold name
                    scaffold_name = str.lstrip(contents)
                    nuc_sequences[scaffold_name] = ""
                 else: #Line is part of DNA sequence
                    nuc_sequences[scaffold_name] += str.lstrip(contents)
                 contents = unzipped.readline()
             unzipped.close()
             all_nuc_sequences[label] = nuc_sequences
            except:
                pass
        print("Finished reading database")
        return [labels, all_nuc_sequences]