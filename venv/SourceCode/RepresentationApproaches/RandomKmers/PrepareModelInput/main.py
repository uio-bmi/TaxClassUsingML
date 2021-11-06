from count_transformer import CountTransformer
import csv

transformer = CountTransformer()
# Parameters are: speciesLevel and countBased
transformer.doTransformation(False, False)
vectors = transformer.getVectors()
labels = transformer.getLabels()

# Write vectors to file
with open("all_vectors.txt", "w") as file:
    csv.writer(file, delimiter=" ").writerows(vectors)

# Write labels to file
with open("all_labels.txt", "w") as file:
    csv.writer(file, delimiter=" ").writerows(labels)