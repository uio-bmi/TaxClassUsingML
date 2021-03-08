import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
from FastaGeneDataset import FastaGeneDataset

# Use FASTA file to create a dataset object.
file = open("gg_12_10.fasta", "r")
dataset = FastaGeneDataset(file, 6)
file.close()

# Prepare training set and training labels.
training_set = dataset.getTrainingSet()
training_labels = dataset.getTrainingLabels()

input_shape = len(training_set[0])

# Create neural network

# 68
model = tf.keras.Sequential([
    layers.Flatten(input_shape=(input_shape,)),
    layers.Dense(400, activation='relu'),
    layers.Dense(101)
])


# Build model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy']
              )

# Train model
model.fit(training_set, training_labels, epochs=100)

# Check model accuracy
test_loss, test_acc = model.evaluate(training_set, training_labels, verbose=2)
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