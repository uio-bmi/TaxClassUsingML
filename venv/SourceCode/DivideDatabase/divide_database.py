import csv
import random
import math
import os

# Class is used to divide the database into a training set, validation set, and test set.
class DivideDatabase:

    @staticmethod
    def divideDatabase():
        temp = DivideDatabase.__selectSetDivision()
        validation_set = temp[0]
        test_set = temp[1]

        #Move files into validation set
        for file in validation_set:

            try:
              os.replace("./TrainingSet/" + file + "_genomic.fna.gz",
                         "./ValidationSet/" + file + "_genomic.fna.gz")
            except:
                pass


        #Move files into test set
        for file in test_set:
            print(file)
            try:
                os.replace("./TrainingSet/" + file + "_genomic.fna.gz",
                           "./TestSet/" + file + "_genomic.fna.gz")
            except:
                pass

    @staticmethod
    def __selectSetDivision():
        # Add all file names to training set
        training_set = []
        file = open("./gtdb_taxonomy.tsv", encoding="utf8")
        reader = csv.reader(file, delimiter="\t", quotechar='"')
        for row in reader:
          file_name = row[0].replace("GB_", "").replace("RS_", "")
          training_set.append(file_name)

        # Select random files for the validation set.
        validation_set = []
        size_of_validation_set = math.floor((len(training_set) / 100) * 30)
        for i in range(0, size_of_validation_set):
            selected_file = random.randint(0, len(training_set))
            validation_set.append(training_set[selected_file]) #Add file to validation set.
            del training_set[selected_file]

        # Select random files for the test set.
        test_set = []
        size_of_test_set = math.floor(((len(training_set) + len(validation_set)) / 100) * 20)
        for i in range(0, size_of_test_set):
            selected_file = random.randint(0, len(training_set))
            test_set.append(training_set[selected_file]) #Add file to test set.
            del training_set[selected_file]

        print("Length training set: ", len(training_set))
        print("Length validation set: ", len(validation_set))
        print("Length test set: ", len(test_set))
        return [validation_set, test_set]



