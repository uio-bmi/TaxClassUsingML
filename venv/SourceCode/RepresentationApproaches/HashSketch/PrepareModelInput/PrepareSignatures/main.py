from signature_transformer import SignatureTransformer
import json
import csv
import numpy as np
from numpy import loadtxt

# Transform set of sourmash signature files into vector representations.

transformer = SignatureTransformer()
# Parameter: speciesLevel
transformer.doTransformation(False)
signatures = transformer.getSignatures()
labels = transformer.getLabels()

# Write signatures to file
with open("all_vectors.txt", "w") as file:
    csv.writer(file, delimiter=" ").writerows(signatures)

# Write labels to file
with open("all_labels.txt", "w") as file:
    csv.writer(file, delimiter=" ").writerows(labels)
