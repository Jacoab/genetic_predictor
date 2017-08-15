#
# Programed By: Jake Jongewaard
# Description: routines for loading amazon fine food reviews
#================================================================


#TODO: implement multithreading for reading and reformating


import csv
import numpy as np


BATCH_SIZE = 250


def read_reviews(filename):
    """
    Reads a csv file of fine food reviews and loads the reviews
    into a numpy array

    :param filename:
    :return: 2-dimensional numpy array that holds each batch of reviews
    """
    batches = np.array()
    count = 0

    with open(filename, 'rb') as reviews_csv:
        reader = csv.reader(reviews_csv)
        for row in reader:
            batch_buff = np.array()

            if count % BATCH_SIZE is 0:
                np.append(batches, batch_buff)
            else:
                np.append(batch_buff, row[9])

            count += 1

    return batches


def get_all_words(review_batch):
    """
    Break reviews into a numpy array of individual words

    :param review_batch: numpy array holding a Batch of review strings
    :return: Individual review strings
    """
    delim = ' '
    word_array = np.array()
    start_index = 0
    delim_index = 0

    """
    Iterate through each character in each review until the delimiter
    is reached. Once the delimiter is reached, append the word given at
    start_index to delim_index-1
    """
    for review in review_batch:
        for i in range(0, len(review) - 1):

            if review[i] == delim:
                delim_index = i
                np.append(word_array, review[start_index:delim_index-1])
                start_index = i + 1

        start_index = 0
        delim_index = 0

    return word_array





