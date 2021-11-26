from transform_kmers import CountTransformer
import csv

# Transform set of k-mer counts into representation vectors.

transformer = CountTransformer()
# Parameter is: speciesLevel
transformer.doTransformation(False)
vectors = transformer.getVectors()
labels = transformer.getLabels()

# Write vectors to file
with open("all_vectors.txt", "w") as file:
    csv.writer(file, delimiter=" ").writerows(vectors)

# Write labels to file
with open("all_labels.txt", "w") as file:
    csv.writer(file, delimiter=" ").writerows(labels)