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

    # 0,0018  0,0018  0,0018
    def getBasicModel1(self):
        return Sequential([
               layers.Flatten(input_shape=(self.input_shape,)),
               layers.Dense(self.species, activation='relu'),
               layers.Dense(self.species)
        ])

    # 0,0037  0,0037  0,0037
    def getBasicModel2(self):
        return Sequential([
               layers.Flatten(input_shape=(self.input_shape,)),
               layers.Dense(self.species, activation='relu'),
               layers.Dense(self.species, activation='relu'),
               layers.Dense(self.species)
        ])

    # 0,0037  0,0037 0,0037
    def getBasicModel3(self):
        return Sequential([
            layers.Dense(self.species, input_shape=(self.input_shape,), activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species)
        ])

    # 0,0037  0,0037  0,0037
    def getBasicModel4(self):
        return Sequential([
            layers.Dense(self.species, input_shape=(self.input_shape,), activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species)
        ])

    # 0,0018  0,0018  0,0037
    def getBasicModel5(self):
        return Sequential([
            layers.Dense(self.species, input_shape=(self.input_shape,), activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species)
        ])

    # 0,0037  0,0037  0,0037
    def getBasicModel6(self):
        return Sequential([
            layers.Dense(self.species, input_shape=(self.input_shape,), activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species)
        ])

    # 0,0037  0,0018  0,0018
    def getBasicModel7(self):
        return Sequential([
            layers.Dense(self.species, input_shape=(self.input_shape,), activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species, activation='relu'),
            layers.Dense(self.species)
        ])
