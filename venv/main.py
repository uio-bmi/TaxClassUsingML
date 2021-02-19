import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import numpy as np
from FastaGeneDataset import FastaGeneDataset

# Use FASTA file to create a dataset object.
file = open("gg_12_10.fasta", "r")
dataset = FastaGeneDataset(file, 6)
file.close()

# Prepare training set and training labels.
training_set = dataset.getTrainingSet()
training_labels = []
for x in range(100):
    training_labels.append(float(x))
training_labels = np.array(training_labels, dtype=np.float)

input_shape = len(training_set[0])

# Create neural network
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(input_shape,)),
    tf.keras.layers.Dense(300, activation='relu'),
    tf.keras.layers.Dense(100)
])

#inputs = tf.keras.Input(shape=(1500))
#x = tf.keras.layers.Dense(1360, activation='relu')(inputs)
#x = tf.keras.layers.Dense(1360, activation='relu')(x)
#outputs = tf.keras.layers.Dense(100, activation='softmax')(x)
#model = tf.keras.Model(inputs=inputs, outputs=outputs)

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