import numpy as np
from prepare_signs import PrepareSigns
import json
import csv
from numpy import loadtxt
import pickle
import numpy as np

transformer = PrepareSigns()
transformer.doTransformation()
signatures = transformer.getSignatures()
labels = transformer.getLabels()
labels = np.array(labels, dtype=str)

# Write signatures to file
with open("all_vectors.txt", "w") as file:
    csv.writer(file, delimiter=" ").writerows(signatures)

# Write labels to file
with open("all_labels.txt", "w") as file:
    for label in labels:
        file.write(label + "\n")
