# TaxClassUsingML
The code in this repository is part of the master thesis: Comparing Artifical Neural Networks and Microbial Genome Representation Methods for Taxonomic Classification

This thesis was submited in the autumn 2021.

# Project Description

This master thesis explores taxonomic classification on whole genome data by performing direct comparisons on different ways of representing a genome through k-mers and 
testing on different types of neural networks. A training, validation, and test set was made from the GTDB database which covers a wide range of bacterial and archaea 
whole genomes. These genomes were transformed into k-mer representation vectors using the following methods: MinHash sketching, frequencies of random k-mers, presence of 
random k-mers, and discriminative k-mers. Each of these methods were tested on a set of three different artificial neural networks, standard neural network, multilayer 
perceptron network, and convolutional neural network. All models were measured for accuracy and precision on a test set to determine the combination of representation 
method and model that would be the most suitable for taxonomic classification of microorganisms.
