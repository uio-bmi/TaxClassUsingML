import os
import gzip

class UniqueKmerSelector:
    unique_kmers = {}
    useless_kmers = {} #kmers which exist in more than one file

    # Method adds a kmer to the class dictionaries.
    def __addToDictionary(self, kmer):
        if kmer in self.unique_kmers or kmer[::-1] in self.unique_kmers:
            try:
                del self.unique_kmers[kmer]
                self.useless_kmers[kmer] = 1
            except:
                pass
        else:
            self.unique_kmers[kmer] = 1

    # Method goes through a file and adds every kmer to the class dictionaries.
    def __findUselessKmersInFile(self, file):
        with gzip.open(file, "rt") as f:
            for line in f:
                if line.find(">"):
                    self.__addToDictionary(line.rstrip("\n"))
        f.close()

    # Method returns an array of all files in the Counts folder.
    @staticmethod
    def __getFileNames(directory):
        print("Finding file names...")
        path = "./" + directory + "/"
        files = []
        for file in os.listdir(path):
            fullpath = os.path.join(path, file)
            files.append(fullpath)
        print("Finished finding file names")
        return files


    def prepareFiles(self):
        files = self.__getFileNames("Counts")
        for i in range(len(files)):
            os.renames(files[i], "./Unique/" +
                       files[i].replace(".fna.gz.fa.gz", "").replace("./Counts/", "") + ".fna.gz")


    # Method goes through every file in the Counts folder and removes common kmers.
    def stripFiles(self):
        telle = 0
        files = self.__getFileNames("Unique")

        #For each file in the folder...
        for i in range(len(files)):
            print("Working on file ", i)
            starter_file = files[i]
            comparison_pointer = i + 1 #Points to file we are comparing starter_file to

            #Compare every file to the starter file, finding common kmers
            while comparison_pointer < len(files):
                comparison_file = files[comparison_pointer]
                self.__findUselessKmersInFile(starter_file)
                self.__findUselessKmersInFile(comparison_file)
                self.unique_kmers.clear()
                self.__removeUselessKmers(starter_file)
                telle = telle + 1
                removal_pointer = comparison_pointer

                #Remove common kmers with starter file from every other file.
                while removal_pointer < len(files):
                    self.__removeUselessKmers(files[removal_pointer])
                    removal_pointer = removal_pointer + 1
                    telle = telle + 1

                comparison_pointer = comparison_pointer + 1
            print("telle", telle)

    # Method replaces old file with a new file where the useless kmers are gone.
    def __removeUselessKmers(self, file):
        clean_file = open(file + "_temp.fna.gz", "w+") #Create replacement file
        file = gzip.open(file, "rt")
        content_arr = file.read().split(">")
        for elem in content_arr:
            try:
                kmer = elem.split("\n")[1]
                #Write kmers to new file unless they are useless
                if kmer not in self.useless_kmers:
                    temp = ">\n" + kmer + "\n"
                    clean_file.write(temp)
            except:
                pass
        file.close()
        clean_file.close()
        file_name = file.name
        os.remove(file.name)
        os.renames(file_name + "_temp.fna.gz", file_name)
