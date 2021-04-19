# coding=utf-8

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras import layers
import numpy as np
from fasta_gene_dataset import FastaGeneDataset
from PreProcessing.trash_remover import TrashRemover

TrashRemover.clean()

# Use FASTA file to create a dataset object.
dataset = FastaGeneDataset(31)

# Prepare training set and training labels.
training_set = dataset.getTrainingSet()
training_labels = dataset.getTrainingLabels()
test_set = dataset.getTestSet()
test_labels = dataset.getTestLabels()

# Create neural network
input_shape = len(training_set[0])
labels = len(training_labels)

species = 31911

# 10 runder liten database: 88
basic_model = Sequential([
    layers.Flatten(input_shape=(input_shape,)),
    layers.Dense(100, activation='relu'),
    layers.Dense(400, activation='relu'),
    layers.Dense(species)
])

#10 runder liten database: 86
basic_model2 = Sequential([
    layers.Dense(100, input_shape=(input_shape,), activation='relu'),
    layers.Dense(400, activation='relu'),
    layers.Dense(400, activation='relu'),
    layers.Dense(species)
])

total_num_words = dataset.getTotalCountKmers()

#10 runder liten database: 30
cnn_model = tf.keras.Sequential([
    layers.Embedding(input_dim=total_num_words, output_dim=100),
    layers.Conv1D(128, 5, activation='relu'),
    layers.AveragePooling1D(pool_size=2, padding='valid'),
    layers.Conv1D(128, 5, activation='relu'),
    layers.AveragePooling1D(pool_size=2, padding='valid'),
    layers.Dense(64, activation='relu'),
    layers.GlobalAveragePooling1D(),
    layers.Dense(species, activation='softmax')
])

model = basic_model

#model.summary()

# Build model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy']
              )
# Train model
model.fit(training_set, training_labels, epochs=10)

# Check model accuracy
test_loss, test_acc = model.evaluate(test_set, test_labels, verbose=2)
print('\nModel accuracy: ', test_acc)
print('\nModel loss: ', test_loss)

model = basic_model2

#model.summary()

# Build model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy']
              )
# Train model
model.fit(training_set, training_labels, epochs=10)

# Check model accuracy
test_loss, test_acc = model.evaluate(test_set, test_labels, verbose=2)
print('\nModel accuracy: ', test_acc)
print('\nModel loss: ', test_loss)

model = cnn_model

#model.summary()

# Build model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy']
              )
# Train model
model.fit(training_set, training_labels, epochs=10)

# Check model accuracy
test_loss, test_acc = model.evaluate(test_set, test_labels, verbose=2)
print('\nModel accuracy: ', test_acc)
print('\nModel loss: ', test_loss)

# Add probability layer to model for prediction
#probability_model = tf.keras.Sequential([
#    model,
#    tf.keras.layers.Softmax()
#])

# Make prediction for each element in test set
#predictions = probability_model.predict(training_set)

#test = training_set[23]
#test = (np.expand_dims(test, 0))
#predic = probability_model.predict(test)
#print(predic)