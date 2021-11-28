from transform_kmers import DiscriminativeTransformer
import csv

# Transform set of discriminative k-mers into representation vectors.

transformer = DiscriminativeTransformer()
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