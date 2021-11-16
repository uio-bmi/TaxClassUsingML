import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras import layers
import numpy as np

class ConvolutionalModels:

    input_shape = 0
    species = 0

    def __init__(self, input_shape, species):
        self.input_shape = input_shape
        self.species = species

    # 0.00012
    def getConvoModel1(self, timesteps, features, outputs):
        return tf.keras.Sequential([
            layers.Conv1D(filters=1, strides=1, activation="relu", input_shape=(timesteps, features), kernel_size=1),
            layers.Dense(outputs, activation="softmax")
        ])

    # 0.0004
    def getConvoModel2(self, timesteps, features, outputs):
        return tf.keras.Sequential([
            layers.Conv1D(filters=1, strides=1, activation="relu", input_shape=(timesteps, features), kernel_size=1),
            layers.Conv1D(filters=1, strides=1, activation="relu", kernel_size=1),
            layers.Conv1D(filters=1, strides=1, activation="relu", kernel_size=1),
            layers.Dense(outputs, activation="softmax")
        ])

    # 0.0001
    def getConvoModel3(self, timesteps, features, outputs):
        return tf.keras.Sequential([
            layers.Conv1D(filters=64, strides=1, activation="relu", input_shape=(timesteps, features), kernel_size=1, padding="valid"),
            layers.Conv1D(filters=64, strides=1, activation="relu", kernel_size=1, padding="valid"),
            layers.GlobalMaxPooling1D(),
            layers.Dense(outputs, activation="softmax")
        ])

    # 0.0001
    def getConvoModel4(self, timesteps, features, outputs):
        return tf.keras.Sequential([
            layers.Conv1D(filters=64, strides=1, activation="relu", input_shape=(timesteps, features), kernel_size=1, padding="valid"),
            layers.Conv1D(filters=64, strides=1, activation="relu",kernel_size=1, padding="valid"),
            layers.Dense(self.species, activation="relu"),
            layers.Dense(outputs, activation="softmax")
        ])

    # 0
    def getConvoModel5(self, timesteps, features, outputs):
        return tf.keras.Sequential([
            layers.Conv1D(128, 5, activation='relu', input_shape=(timesteps, features)),
            layers.AveragePooling1D(pool_size=2, padding='valid'),
            layers.Conv1D(128, 5, activation='relu'),
            layers.AveragePooling1D(pool_size=2, padding='valid'),
            layers.Dense(64, activation='relu'),
            layers.GlobalAveragePooling1D(),
            layers.Dense(outputs, activation='softmax')
        ])

    # 0
    def getConvoModel6(self, timesteps, features, outputs):
        return tf.keras.Sequential([
            layers.Conv1D(filters=64, strides=1, activation="relu", input_shape=(timesteps, features), kernel_size=1, padding="valid"),
            layers.AveragePooling1D(pool_size=2, padding='valid'),
            layers.Conv1D(filters=64, strides=1, activation="relu", kernel_size=1, padding="valid"),
            layers.GlobalAveragePooling1D(),
            layers.Dense(self.species, activation="relu"),
            layers.Dense(outputs, activation="softmax")
       ])