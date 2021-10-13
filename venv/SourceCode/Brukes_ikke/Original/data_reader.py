import os
import gzip
import csv

class DataReader:

    # Method reads the species label for each file in the database and transfers
    # those to a set which is then returned.
    @staticmethod
    def readSpeciesNames():
        labels = {}
        labels_file = open("./SourceCode/gtdb_taxonomy.tsv", encoding="utf8")
        label_reader = csv.reader(labels_file, delimiter="\t", quotechar='"')
        for row in label_reader:
            labels[row[0]] = row[1]
        return labels

    # Method reads the database and returns an array of all lables and a set of all
    # DNA sequences in the database.
    @staticmethod
    def readDataFiles():
        #Open each database file
        print("Reading database...")
        path = "./SourceCode/Database/"
        labels = []
        all_nuc_sequences = {}
        #For each file in the database
        for file in os.listdir(path):
            fullpath = os.path.join(path, file)
            file_name = "GB_" + file.replace("_genomic.fna.gz", "")
            labels.append(file_name)
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
             all_nuc_sequences[file_name] = nuc_sequences
            except:
                pass
        print("Finished reading database")
        return [labels, all_nuc_sequences]
