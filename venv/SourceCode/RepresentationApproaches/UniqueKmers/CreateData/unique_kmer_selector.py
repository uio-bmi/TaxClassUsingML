import os
import gzip

class UniqueKmerSelector:
    unique_kmers = {} #K-mers that are unique to a genome
    useless_kmers = {} #K-mers which exist in more than one genome

    # Method adds a k-mer to the class dictionaries. Used to identify unique k-mers.
    def __addToDictionary(self, kmer):
        if kmer in self.unique_kmers or kmer[::-1] in self.unique_kmers:
            try:
                del self.unique_kmers[kmer]
                self.useless_kmers[kmer] = 1
            except:
                pass
        else:
            self.unique_kmers[kmer] = 1

    # Method goes through a file and adds every k-mer to the class dictionaries.
    def __findUselessKmersInFile(self, file):
        with open(file, "rt", encoding="utf8") as f:
            for line in f:
                if line.find(">"):
                    self.__addToDictionary(line.rstrip("\n"))
        f.close()

    # Method returns an array of all files in the the given folder.
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


    # Method goes through every file in the folder og k-mer counts and removes common k-mers.
    def stripFiles(self):
        files = self.__getFileNames("Counts")

        #For each file in the folder...
        for i in range(len(files)):
            print("Working on file " + i + files[i])
            starter_file = files[i]
            comparison_pointer = i + 1 #Points to file we are comparing starter_file to

            #Compare every file to the starter file, finding common kmers
            while comparison_pointer < len(files):
                comparison_file = files[comparison_pointer]
                self.__findUselessKmersInFile(starter_file)
                self.__findUselessKmersInFile(comparison_file)
                self.unique_kmers.clear()
                self.__removeUselessKmers(starter_file)
                removal_pointer = comparison_pointer

                if len(self.useless_kmers) > 0:
                   #Remove common kmers with starter file from every other file.
                   while removal_pointer < len(files):
                       self.__removeUselessKmers(files[removal_pointer])
                       removal_pointer = removal_pointer + 1

                self.unique_kmers.clear()
                comparison_pointer = comparison_pointer + 1

            os.rename(starter_file, "./Finished/" + starter_file.replace("./Counts/", ""))


    # Method replaces old k-mer count file with a new file where the useless kmers are gone.
    def __removeUselessKmers(self, file):
        clean_file = open(file + "_temp", "w+") #Create replacement file
        try:
          file = open(file, "rt")
          content_arr = file.read().split(">")
          for elem in content_arr:
             try:
                kmer = elem.split("\n")[1]
                #Write kmers to new file unless they are useless
                if kmer not in self.useless_kmers and kmer[::-1] not in self.useless_kmers:
                    temp = ">\n" + kmer + "\n"
                    clean_file.write(temp)
             except:
                pass

          file.close()
          clean_file.close()
          file_name = file.name
          os.remove(file.name)
          os.renames(file_name + "_temp", file_name)
        except:
            pass
