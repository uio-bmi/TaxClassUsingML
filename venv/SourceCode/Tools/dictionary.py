# This class holds two dictionaries. The index dictionary associates each key with a unique index.
# The counter dictionary counts the number of times a key is attempted added to the dictionary. The
# counter dictionay is optional.

class Dictionary:

    __counterDictionary = {} # Count key frequencies
    __indexDictionary = {} # Associate key with index

    def __init__(self, useCounterDictionary):
        # The first element in a dictionary is reserved as empty placeholder data.
        self.__indexDictionary["None"] = 0
        if useCounterDictionary:
            self.__counterDictionary["None"] = 0


    def getDictionaryLength(self):
        return len(self.__indexDictionary)

    # METHODS FOR COUNTER DICTIONARY

    # Method returns the counter dictionary.
    def getCounterDictionary(self):
        return self.__counterDictionary

    # Method adds a set to the counter dictionary.
    def addSetToCounterDictionary(self, setOfKeys):
        for key in setOfKeys:
            self.__addToCounterDictionary(key)

    # Method adds a key to the counter dictionary.
    def __addToCounterDictionary(self, key):
        if key in self.__counterDictionary:
            self.__counterDictionary[key] += 1
        else:
            self.__counterDictionary[key] = 1

    # Method removes elements from counter dictionary if the counter is above the given treshold.
    def counterDictionaryCommonalityThresholdRemoval(self, commonalityTreshold):
        toBeDeleted = []
        for elem in self.__counterDictionary.keys():
            if self.__counterDictionary.get(elem) > commonalityTreshold:
                toBeDeleted.append(elem)
        for elemToBeDeleted in toBeDeleted:
            del self.__counterDictionary[elemToBeDeleted]


    # METHODS FOR INDEX DICTIONARY

    # Method returns the index dictionary
    def getIndexDictionary(self):
        return self.__indexDictionary

    # Method adds as set of keys to the index dictionary.
    def addSetToDictionary(self, setOfKeys):
        for key in setOfKeys:
            self.addToIndexDictionary(key)

    # Method adds an element to the index dictionary.
    def addToIndexDictionary(self, key):
        self.__indexDictionary[key] = len(self.__indexDictionary)
