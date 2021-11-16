import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras import layers
import numpy as np

class MoreNeuralNetworks:

    input_shape = 0
    species = 0

    def __init__(self, input_shape, species):
        self.input_shape = input_shape
        self.species = species

    def getBasicModel1(self, timesteps, features, outputs):
        return Sequential([
               layers.Dense(input_shape=(timesteps, features)),
               layers.Dense(self.species, activation='relu'),
               layers.Dense(outputs, activation='softmax')
        ])

    def getBasicModel2(self, timesteps, features, outputs):
        return Sequential([
            layers.Dense(self.species, input_shape=(timesteps, features), activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(outputs, activation="softmax")
    ])

    def getBasicModel3(self):
        return Sequential([
            layers.Dense((self.species/2), input_shape=(self.input_shape,), activation='relu'),
            layers.Dense((self.species/2), activation='relu'),
            layers.Dense((self.species/2), activation='relu'),
            layers.Dense((self.species/2), activation='relu'),
            layers.Dense((self.species/2), activation='relu'),
            layers.Dense((self.species/2), activation='relu'),
            layers.Dense((self.species/2), activation='relu'),
            layers.Dense(self.species, activation="softmax")
    ])

    def getBasicModel4(self):
        return Sequential([
            layers.Dense(self.species, input_shape=(self.input_shape,), activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation="softmax")
    ])

    def getBasicModel5(self):
        return Sequential([
            layers.Dense((self.species/2), input_shape=(self.input_shape,), activation='relu'),
            layers.Dense((self.species/2), activation='relu'),
            layers.Dense((self.species/2), activation='relu'),
            layers.Dense((self.species/2), activation='relu'),
            layers.Dense((self.species/2), activation='relu'),
            layers.Dense((self.species/2), activation='relu'),
            layers.Dense((self.species/2), activation='relu'),
            layers.Dense((self.species/2), activation='relu'),
            layers.Dense((self.species/2), activation='relu'),
            layers.Dense((self.species/2), activation='relu'),
            layers.Dense(self.species, activation="softmax")
    ])

    def getBasicModel6(self):
        return Sequential([
            layers.Dense(self.species, input_shape=(self.input_shape,), activation='relu'),
            layers.Dense((self.species/2), activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense((self.species/2), activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense((self.species/2), activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense((self.species/2), activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense((self.species/2), activation='relu'),
            layers.Dense(self.species, activation="softmax")
    ])