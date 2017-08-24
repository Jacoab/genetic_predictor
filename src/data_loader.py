#
# Programed By: Jake Jongewaard
# Description: routines for loading amazon fine food reviews
#================================================================


#TODO: implement multithreading for reading and reformating


import csv
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


def get_all_words(review_batch):
    """
    Break reviews into a numpy array of individual words

    :param review_batch: numpy array holding a Batch of review strings
    :return: Individual review strings
    """
    delim = ' '
    word_list = []
    start_index = 0
    delim_index = 0

    """
    Iterate through each character in each review until the delimiter
    is reached. Once the delimiter is reached, append the word given at
    start_index to delim_index-1
    """
    for review in review_batch:
        for i in range(0, len(review)):

            if review[i] == delim:
                delim_index = i
                word_list.append(review[start_index:delim_index])
                start_index = i + 1

        start_index = 0
        delim_index = 0

    return np.array(word_list)





