#
# Programed By: Jake Jongewaard
# Description: routines for loading amazon fine food reviews
#================================================================


import csv
import multiprocessing as mp
import numpy as np
import pandas as pd


BATCH_SIZE = 50000
TOTAL_TRAINING_SIZE = 500000


def read_reviews(filename):
    """
    Reads a csv file of fine food reviews and loads the reviews
    into a numpy array

    :param filename:
    :return: 2-dimensional numpy array that holds each batch of reviews
    """
    review_csv = pd.read_csv(filename)
    review_array = np.array(review_csv.Text)
    trimmed_review_array = review_array[0:500000]

    review_batches = np.split(trimmed_review_array, 10)
    return review_batches


def _read_subbatch_words(subbatch):
    """
    Iterate through each character in each review until the delimiter
    is reached. Once the delimiter is reached, append the word given at
    start_index to delim_index-1

    :param subbatch: subbatch of reviews to read from
    :return: A list of individual words in the subbatch
    """
    start_index = 0
    word_list = []
    delim = ' '

    for review in subbatch:
        for i in range(0, len(review)):

            if review[i] == delim:
                delim_index = i
                word_list.append(review[start_index:delim_index])
                start_index = i + 1

        start_index = 0

    return word_list


def get_word_batches(batch, num_of_subbatches):
    """
    Convenience method for reading multiple subbatches of a
    batch in multiple processes in order to speed up reading.

    :param batch: Batch to read from
    :param num_of_subbatches: Number of subbatches to be used
    :return: List batches of individual words
    """
    subbatches = np.split(batch, num_of_subbatches)

    pool = mp.Pool(num_of_subbatches)
    return pool.map(_read_subbatch_words, subbatches)