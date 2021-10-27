import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from unique_kmer_selector import UniqueKmerSelector

# Main method used to run the code which finds a set of unique kmers using the
# UniqueKmerSelector.

selector = UniqueKmerSelector()
selector.stripFiles()