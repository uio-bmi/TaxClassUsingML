# coding=utf-8
import json
import os
import os.path
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from Models.neural_networks import NeuralNetworks
from Models.convolutional_networks import ConvolutionalNetworks
from numpy import loadtxt

# Main file used to train and test neural networks.

# Method returns a set. Either the set for training, validation, or test
# based on given parameter. Input must be string training, validation or test.
def getSet(set_type):
    vectors = loadtxt(set_type + "_vectors.txt", delimiter=" ", unpack=False)
    vectors = np.array(vectors, dtype=float)
    labels = loadtxt(set_type + "_labels.txt", delimiter=" ", unpack=False)
    labels = np.array(labels, dtype=float)
    return [vectors, labels]

# Fetch sets like this, files must be in the same folder as this class:
training_set, training_labels = getSet("training")
validation_set, validation_labels = getSet("validation")
test_set, test_labels = getSet("test")

# Convolutional neural network requires the data be reshaped in the following way.
#training_set = training_set.reshape(len(training_set), len(training_set[0]), 1)
#training_labels = training_labels.reshape(len(training_labels), len(training_labels[0]))
#validation_set = validation_set.reshape(len(validation_set), len(validation_set[0]), 1)
#validation_labels = validation_labels.reshape(len(validation_labels), len(validation_labels[0]))
#test_set = test_set.reshape(len(test_set), len(training_set[0]), 1)
#test_labels = test_labels.reshape(len(test_labels), len(test_labels[0]))

# Models require the following parameters.
features = len(training_set[0])
classes = len(training_labels[0])

# Method trains a model
def trainModel(model, name):
    # Build model
    model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.1),
                  loss=tf.keras.losses.CategoricalCrossentropy(from_logits=False),
                  metrics=['accuracy', tf.keras.metrics.Precision()]
                  )
    # Train model
    model.fit(training_set, training_labels, epochs=10, shuffle=True,
              validation_data=(validation_set, validation_labels), verbose=2)
    model.save("Models/" + name + ".h5")

# Method tests a model on a given set.
def testModel(model):
    # Check model accuracy and precision
    test_loss, test_prec, test_acc = model.evaluate(test_set, test_labels, verbose=2)
    print('\nModel precision: ', test_prec)
    print('\nModel accuracy: ', test_acc)
    print('\nModel loss: ', test_loss)

models = NeuralNetworks(features, classes)
convoModels = ConvolutionalNetworks(features, classes)

# Train and test standard neural network
standard = models.getStandardNeuralNetwork()
trainModel(standard, "standard")
testModel(standard)

# Train and test multi-layer perceptron neural network.
multi = models.getPerceptronNetwork()
trainModel(multi, "multi")
testModel(multi)

# Train and test convolutional neural network.
convo = convoModels.getConvolutionalNeuralNetwork()
trainModel(convo, "convo")
testModel(convo)





