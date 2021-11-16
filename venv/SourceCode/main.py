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
from Models.convolutional_neural import ConvolutionalModels
from Models.more_neural import MoreNeuralNetworks
from numpy import loadtxt

# Importing MinHash training set
signatures = loadtxt("all_vectors.txt", delimiter=" ", unpack=False)
signatures = np.array(signatures, dtype=float)
labels = loadtxt("all_labels.txt", delimiter=" ", unpack=False)
labels = np.array(labels, dtype=float)
training_set = signatures
training_labels = labels

# Import MinHash test set
test_signatures = loadtxt("test_vectors.txt", delimiter=" ", unpack=False)
test_signatures = np.array(test_signatures, dtype=float)
test_labels = loadtxt("test_labels.txt", delimiter=" ", unpack=False)
test_labels = np.array(test_labels, dtype=float)
test_set = test_signatures
test_labels = test_labels

# For vanlige nettverk
input_shape = len(training_set[0])
species = len(training_labels[0])
models = MoreNeuralNetworks(input_shape, species)

# For convolutional nettverk
# training_set = training_set.reshape((5, 40000))
# training_labels = training_labels.reshape((5, len(training_labels[0])))
# test_set = test_set.reshape((5, 40000))
# test_labels = test_labels.reshape((5, len(test_labels[0])))
#timesteps = training_set.shape[1]
#features = training_set.shape[2]
#outputs = training_labels[1]
#input_shape = tf.shape(training_set)
#species = len(training_labels[0])
#models = ConvolutionalModels(input_shape, species)

def runModel(model):
    # Build model
    model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.1),
                  loss=tf.keras.losses.MeanAbsoluteError(),
                  metrics=['accuracy']
                  )
    # Train model
    model.fit(training_set, training_labels, epochs=10)
    # Check model accuracy
    test_loss, test_acc = model.evaluate(test_set, test_labels, verbose=2)
    print('\nModel accuracy: ', test_acc)
    print('\nModel loss: ', test_loss)

model = models.getBasicModel1()
runModel(model)
model = models.getBasicModel2()
runModel(model)
model = models.getBasicModel3()
runModel(model)
model = models.getBasicModel4()
runModel(model)
model = models.getBasicModel5()
runModel(model)
model = models.getBasicModel6()
runModel(model)
