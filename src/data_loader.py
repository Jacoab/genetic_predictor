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
        for row in reader:  #possibly use a range without a count
            batch_buff = np.array()

            if count % BATCH_SIZE is 0:
                np.append(batches, batch_buff)
            else:
                np.append(batch_buff, row[9])

            count += 1

    return batches


def get_all_words(review_batch):
    delim = ' '
    word_array = np.array()
    count = 0
    delim_index = 0
    for review in review_batch:
        for char in review:

            if char == delim:
                delim_index = count + 1
                np.append(word_array, review[delim_index+1:(delim_index+1)+count])
            else:
                count += 1

        count = 0
        delim_index = 0

    return word_array





