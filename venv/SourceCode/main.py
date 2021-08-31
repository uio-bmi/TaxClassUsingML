# coding=utf-8
import json
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras import layers
import numpy as np
from Cleaning.trash_remover import TrashRemover
from RepresentationApproaches.SketchSignatures.minhash_input import MinHashInput
#from RepresentationApproaches.UniqueKmers.unique_kmer_selector import UniqueKmerSelector
from Models.basic_neural import BasicModel

#selector = UniqueKmerSelector()
#uniq = selector.findUniqueKmers()


#count = 0
#for key in uniq.keys():
#    print("key ", key)
#    print(uniq[key])
#    count = count + 1
#    if count == 5:
#        break


temp = MinHashInput.getTrainingSet()
matrix = temp[0]
labels = temp[1]

training_set = matrix
training_labels = labels

input_shape = len(training_set[0])

species = 31911
species = len(training_labels) + 1
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


#cnn_model = tf.keras.Sequential([
#    layers.Conv1D(filters=1, kernel_size=1, activation="relu", input_shape=(1, 11), name="dette"),
#    layers.Dense(species, activation="softmax")
#])



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
