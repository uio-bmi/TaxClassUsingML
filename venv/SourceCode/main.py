# coding=utf-8
import json
import os

import numpy

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras import layers
import numpy as np
import pandas as pd
from Models.basic_neural import NeuralNetworks
from numpy import loadtxt

# Importing MinHash input
signatures = loadtxt("all_vectors.txt", delimiter=" ", unpack=False)
signatures = np.array(signatures, dtype=float)
labels = []
labelFile = open("all_labels.txt", "r").readlines()
for label in labelFile:
    labels.append(label)
labels = np.array(labels, dtype=float)


training_set = signatures
training_labels = labels

input_shape = len(training_set[0])
species = 31911
species = len(training_labels)
test_set = training_set
test_labels = training_labels

#10 runder liten database: 30
# total_num_words = 65000
#cnn_model = tf.keras.Sequential([
#    layers.Embedding(input_dim=total_num_words, output_dim=100),
#    layers.Conv1D(128, 5, activation='relu'),
#    layers.AveragePooling1D(pool_size=2, padding='valid'),
#    layers.Conv1D(128, 5, activation='relu'),
#    layers.AveragePooling1D(pool_size=2, padding='valid'),
#    layers.Dense(64, activation='relu'),
#    layers.GlobalAveragePooling1D(),
#    layers.Dense(species, activation='softmax')
#])


#cnn_model = tf.keras.Sequential([
#    layers.Conv1D(filters=1, kernel_size=1, activation="relu", input_shape=(1, 11), name="dette"),
#    layers.Dense(species, activation="softmax")
#])

models = NeuralNetworks(input_shape, species)
basic_model = models.getBasicModel1()

def runModel(model):
    # Build model
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy']
                  )
    # Train model
    model.fit(training_set, training_labels, epochs=100)
    # Check model accuracy
    test_loss, test_acc = model.evaluate(test_set, test_labels, verbose=2)
    print('\nModel accuracy: ', test_acc)
    print('\nModel loss: ', test_loss)

runModel(basic_model)
