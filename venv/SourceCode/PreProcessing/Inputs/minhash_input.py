import os
import json
import numpy as np

# This class fetches signatures created using MinHash.
class MinHashInput:

   # Method creates array of signatures and returns the array.
   @staticmethod
   def getTrainingSet():
       training_set = []
       path = "./SourceCode/Signatures/"

       #Go through each signature in folder
       for file in os.listdir(path):
           #Get signature
           temp = open("./SourceCode/Signatures/" + file, encoding="utf8")
           text = temp.read()
           list = json.loads(text)[0]
           signature = list["signatures"][0]["mins"][:100]

           #Transform elements in signature from sequences to floats
           for index, elem in enumerate(signature):
               transformed_elem = str(elem)
               transformed_elem = float(transformed_elem)
               signature[index] = transformed_elem

           #Transform signature to numpy array
           signature = np.array(signature, dtype=np.float)
           signature = signature / 255.0
           training_set.append(signature)

       #Whole training set is numpy array of numpy arrays.
       training_set = np.array(training_set, dtype=np.float)
       training_set = training_set / 255.0
       return training_set