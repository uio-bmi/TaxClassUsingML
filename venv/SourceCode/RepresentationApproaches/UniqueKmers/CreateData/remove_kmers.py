import os

# Code to remove all but one k-mer from file.

for file in os.listdir("./Temp/"):
    kmer = open(os.path.join("./Temp/", file)).readlines()[1]
    clean_file = open(file + "_temp", "w+")
    clean_file.write("\n" + temp)
    file.close()
    clean_file.close()
    file_name = file.name
    os.remove(file.name)
    os.renames(file_name + "_temp", file_name)
