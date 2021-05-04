# coding=utf-8
import json
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras import layers
import numpy as np
from fasta_gene_dataset import FastaGeneDataset
from PreProcessing.trash_remover import TrashRemover
from PreProcessing.Inputs.minhash_input import MinHashInput

training_set = MinHashInput.getTrainingSet()

training_labels = []
for i in range(0, len(training_set)):
    training_labels.append(float(i))

training_labels = np.array(training_labels, dtype=np.float)

print(training_set[0][0])

input_shape = len(training_set[0])
species = 31911
species = len(training_labels)
test_set = training_set
test_labels = training_labels

basicer_model = Sequential([
    layers.Flatten(input_shape=(input_shape,)),
    layers.Dense(50, activation='relu'),
    layers.Dense(50, activation='relu'),
    layers.Dense(species)
])

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

total_num_words = 65000

#10 runder liten database: 30
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


# Check model accuracy
test_loss, test_acc = model.evaluate(test_set, test_labels, verbose=2)
print('\nModel accuracy: ', test_acc)
print('\nModel loss: ', test_loss)

model = basicer_model

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

model = basic_model

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
