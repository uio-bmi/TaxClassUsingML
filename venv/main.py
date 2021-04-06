import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras import layers
import numpy as np
from fasta_gene_dataset import FastaGeneDataset

# Use FASTA file to create a dataset object.
dataset = FastaGeneDataset(31)

# Prepare training set and training labels.
training_set = dataset.getTrainingSet()
training_labels = dataset.getTrainingLabels()



# Create neural network

input_shape = len(training_set[0])

# 68 hvis 100 runder
basic_model = Sequential([
    layers.Flatten(input_shape=(input_shape,)),
    layers.Dense(100, activation='relu'),
    layers.Dense(400, activation='relu'),
    layers.Dense(101)
])

#67 etter 100, læring flater ut etter dette.
basic_model2 = Sequential([
    layers.Dense(100, input_shape=(input_shape,), activation='relu'),
    layers.Dense(400, activation='relu'),
    layers.Dense(400, activation='relu'),
    layers.Dense(101)
])


total_num_words = dataset.getTotalNumberOfKmers()

# 50 hvis 1000 runder
cnn_model = tf.keras.Sequential([
    layers.Embedding(input_dim=total_num_words, output_dim=100),
    layers.Conv1D(128, 5, activation='relu'),
    layers.AveragePooling1D(pool_size=2, padding='valid'),
    layers.Conv1D(128, 5, activation='relu'),
    layers.AveragePooling1D(pool_size=2, padding='valid'),
    layers.Dense(64, activation='relu'),
    layers.GlobalAveragePooling1D(),
    layers.Dense(101, activation='softmax')
])

model = basic_model

model.summary()


# Build model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy']
              )

# Train model
model.fit(training_set, training_labels, epochs=10)

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