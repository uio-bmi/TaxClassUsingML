import math
import random

# Class is used to pick out a test set from the training set.
class GenerateTestSet:

    #The percentage of the total training set which should be used as test set.
    test_set_percentage = 30

    # Method takes the total training set and labels and returns a training set and a test set.
    @staticmethod
    def getDividedSets(training_set, training_labels):
        test_set_indices = GenerateTestSet.__pickTestSetIndices(training_set)
        return GenerateTestSet.__buildTestSet(training_set, training_labels, test_set_indices)

    # Method picks out a set of random indices from a training set to be used as a test set.
    @staticmethod
    def __pickTestSetIndices(all_data):
        test_set_size = math.ceil((len(all_data)/100)*GenerateTestSet.test_set_percentage)
        test_set = []
        for i in range(test_set_size):
            test_element = random.randrange(len(all_data))
            if test_element in test_set:
                test_set_size += 1
            else:
                test_set.append(test_element)
        return test_set

    # Method takes a training set and divides it into a test and training set.
    @staticmethod
    def __buildTestSet(training_set, training_labels, training_set_indices):
        test_set = []
        test_labels = []
        for i in sorted(training_set_indices, reverse=True):
            test_set.append(training_set[i])
            test_labels.append(training_labels[i])
            training_set.pop(i)
            training_labels.pop(i)
        return [test_set, test_labels, training_set, training_labels]