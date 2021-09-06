import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras import layers
import numpy as np

class NeuralNetworks:

    input_shape = 0
    species = 0

    def __init__(self, input_shape, species):
        self.input_shape = input_shape
        self.species = species

    def getBasicModel1(self):
        return Sequential([
               layers.Flatten(input_shape=(self.input_shape,)),
               layers.Dense(50, activation='relu'),
               layers.Dense(50, activation='relu'),
               layers.Dense(self.species)
        ])

    def getBasicModel2(self):
        return Sequential([
               layers.Flatten(input_shape=(self.input_shape,)),
               layers.Dense(100, activation='relu'),
               layers.Dense(400, activation='relu'),
               layers.Dense(self.species)
        ])

    def getBasicModel3(self):
        return Sequential([
            layers.Dense(100, input_shape=(self.input_shape,), activation='relu'),
            layers.Dense(400, activation='relu'),
            layers.Dense(400, activation='relu'),
            layers.Dense(self.species)
        ])
