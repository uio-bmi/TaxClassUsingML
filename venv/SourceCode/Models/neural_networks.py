import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras import layers
import numpy as np

class NeuralNetworks:

    features = 0
    classes = 0

    def __init__(self, features, classes):
        self.features = features
        self.classes = classes

    # Method returns a small, standard neural network.
    def getStandardNeuralNetwork(self):
        return Sequential([
               layers.Dense(self.features, input_shape=(self.features,), activation='relu'),
               layers.Dense(self.features, activation='relu'),
               layers.Dense(self.classes, activation='softmax')
        ])

    # Method returns a multilayer neural network.
    def getPerceptronNeuralNetwork(self):
        return Sequential([
            layers.Dense(self.features, input_shape=(self.features,), activation='relu'),
            layers.Dense(self.features/2, activation='relu'),
            layers.Dense(self.features/2, activation='relu'),
            layers.Dense(self.features/2, activation='relu'),
            layers.Dense(self.features/2, activation='relu'),
            layers.Dense(self.features/2, activation='relu'),
            layers.Dense(self.features/2, activation='relu'),
            layers.Dense(self.classes, activation="softmax")
        ])