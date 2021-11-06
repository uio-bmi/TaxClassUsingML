from random_kmers import KmerGenerator

temp = KmerGenerator.generateRandomKmers(40000, 12)

# Used to check that the correct number of kmers has been generated.
kmers = []
all = []
with open("random_kmers.fa", "r") as file:
  for line in file:
    stripped_line = str(line.strip())
    all.append(stripped_line)
    if ">" not in stripped_line:
       kmers.append(stripped_line)

print("Number of generated kmers: ", len(kmers))
print("Number of lines in random_kmers file: ", len(all))