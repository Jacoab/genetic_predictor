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
print(review_batches, end="")


""" get_all_words(review_batch) test """
print("  Testing get_all_words(review_batch) function with input of review_batches")
print(loader.get_word_batches(review_batches[0], 10))


# for i in range(0, len(all_words)-1):
#     print(all_words[i])
