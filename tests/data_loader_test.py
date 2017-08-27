#
# Programmed By: Jake Jongewaard
#
# Unit test for the utilities provided in the data_loader.py file
#===================================================================

import multiprocessing as mp
import numpy as np

from src import data_loader as loader


REVIEW_FILE = "Reviews.csv"


print("Beginning unit tests of data_loader.py...")


""" read_reviews(filename) test """
print("  Testing read_reviews(filename) function with input of " + REVIEW_FILE)
review_batches = loader.read_reviews(REVIEW_FILE)
print("  ", end="  ")
print(review_batches)


""" get_all_words(review_batch) test """
print("\n  Testing get_all_words(review_batch) function with input of review_batches")
print(sorted(loader.get_words(review_batches[0], 10), key=str.lower))
