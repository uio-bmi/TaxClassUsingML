import csv
import os

# The TrashRemover removes unwanted elements from the database.
class TrashRemover:

 max_contig_count = 200
 max_ambig_count = 100
 min_completeness = 70

 # Method to be called to cleanse the database.
 @staticmethod
 def clean():
   print("Cleaning database...")
   trash = TrashRemover.__getListOfPoorQualityDataObjects()
   TrashRemover.__removeTrashFiles(trash)
   print("Done cleaning")

 # Method returns a list of the data objects not considered
 # complete enough to be used for training.
 @staticmethod
 def __getListOfPoorQualityDataObjects():
   metadata_file = open("./SourceCode/Cleaning/genome_metadata.tsv", encoding="utf8")
   meta_reader = csv.reader(metadata_file, delimiter="\t", quotechar='"')
   next(meta_reader) #Remove table header
   trash = []
   for row in meta_reader:
      if int(row[10]) > TrashRemover.max_contig_count: #contig_count
         trash.append(row)
      elif int(row[1]) > TrashRemover.max_ambig_count: #ambiguous_bases
         trash.append(row)
      elif float(row[2]) < TrashRemover.min_completeness: #checkm_completenes
         trash.append(row)
   return trash

 # Method deletes the files which cannot be used for training.
 @staticmethod
 def __removeTrashFiles(trash_files):
    print(os.getcwd())
    for trashFile in trash_files:
        try:
           os.replace("./Database/" + trashFile[0] + "_genomic.fna.gz",
                      "./UselessData/" + trashFile[0] + "_genomic.fna.gz")
        except:
           trash_files.remove(trashFile)
