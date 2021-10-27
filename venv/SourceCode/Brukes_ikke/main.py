import os

path = "./Signatures/"
signatures = []
for file in os.listdir(path):
    signatures.append(file.replace(".sig", ""))

path = "./Finished/"
finished = []
for file in os.listdir(path):
    finished.append(file)

for file in finished:
    if file not in signatures:
        os.rename("/Finished/" + file, "./TrainingSet/")