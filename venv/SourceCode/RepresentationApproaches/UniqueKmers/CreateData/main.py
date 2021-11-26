import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from unique_kmer_selector import UniqueKmerSelector

# Find unique k-mers in set of k-mer counts.

selector = UniqueKmerSelector()
selector.stripFiles()