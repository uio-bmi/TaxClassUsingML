import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras import layers

class ConvolutionalNetworks:

    features = 0
    classes = 0

    def __init__(self, features, classes):
        self.features = features
        self.classes = classes

    # Method returns a convolutional neural network.
    def getConvolutionalNeuralNetwork(self):
        return tf.keras.Sequential([
             layers.Conv1D(filters=5, strides=1, activation="relu", kernel_size=10, padding='same'),
             layers.Conv1D(filters=5, strides=1, activation="relu", kernel_size=10, padding='same'),
             layers.Dropout(0.5),
             layers.Conv1D(filters=5, strides=1, activation="relu", kernel_size=10, padding='same'),
             layers.Conv1D(filters=5, strides=1, activation="relu", kernel_size=10, padding='same'),
             layers.Dropout(0.5),
             layers.Flatten(),
             layers.Dense(self.features, activation='relu'),
             layers.Dense(self.classes, activation="softmax")
        ])