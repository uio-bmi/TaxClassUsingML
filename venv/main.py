import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import numpy as np
from FastaGeneDataset import FastaGeneDataset

# Use FASTA file to create a dataset object.
file = open("gg_12_10.fasta", "r")
dataset = FastaGeneDataset(file, 8)
file.close()

# Prepare training set and training labels.
training_set = dataset.getTrainingSet()
training_labels = []
for x in range(5):
    training_labels.append(float(x))
training_labels = np.array(training_labels, dtype=np.float)


# Create neural network
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(1500,)),
    tf.keras.layers.Dense(5, activation='relu'),
    tf.keras.layers.Dense(5)
])

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

