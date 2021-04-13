import csv

class LabelFinder:

    labels = {}

    # Method reads the labels for each file in the database and transfers those to a set,
    # which is then returned.
    @staticmethod
    def getLabels():
        labels_file = open("../Data/gtdb_taxonomy.tsv", encoding="utf8")
        label_reader = csv.reader(labels_file, delimiter="\t", quotechar='"')
        for row in label_reader:
            LabelFinder.labels[row[0]] = row[1]
        print(len(LabelFinder.labels))
        return LabelFinder.labels