
from FastaGeneDataset import FastaGeneDataset

# Use FASTA file to create a dataset object.
file = open("gg_12_10.fasta", "r")
dataset = FastaGeneDataset(file)
file.close()

# Test dataset Class methods.
#print(dataset.getElement(1))
#print(dataset.getNumberOfElements())
#print(len(dataset.getAllElements()))
#print(len(dataset.getAnswers()))
#print(len(dataset.getTrainingSet()))

nuc_sequence = dataset.getTrainingElement(3)
kmer_sequence = dataset.seqToKmers(nuc_sequence, 8)

temp = dataset.countKmers(kmer_sequence)

print("Counts: ")
print(len(temp[0]))
print(temp[0])
print("Kmers: ")
print(len(temp[1]))
print(temp[1])