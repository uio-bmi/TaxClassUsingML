from signature_transformer import SignatureTransformer
import json
import csv
import numpy as np
from numpy import loadtxt

transformer = SignatureTransformer()
transformer.doTransformation(False)
signatures = transformer.getSignatures()
labels = transformer.getLabels()

larger = 0
smaller = 0
for signature in signatures:
    count = 0
    for elem in signature:
        if elem == 1:
            count = count + 1
    if count > 3000:
        larger = larger + 1
    if count < 3000:
        smaller = smaller + 1

print("Larger: ", larger)
print("Smaller: ", smaller)

# Write signatures to file
with open("all_vectors.txt", "w") as file:
    csv.writer(file, delimiter=" ").writerows(signatures)

# Write labels to file
with open("all_labels.txt", "w") as file:
    csv.writer(file, delimiter=" ").writerows(labels)
