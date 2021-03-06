#
# Programmed by: Jake Jongewaard
#
# Provides routines for processing data and gathering useful
# statistics.
#==============================================================


import collections
import operator
import random
import re

import numpy as np

from src import data_loader as loader


def _prob_of_next_word(next_word, prev_word_array, review_batch):
    """
    Calculates the probability of of a given word occurring after the previously
    generated words.

    :param next_word: Word to calculate the probability of
    :return: The probability of next_word occurring after the previously generated words
    """
    compare_phrase = np.append(prev_word_array, next_word)
    resized_batch = np.resize(review_batch, (len(compare_phrase)))
    count = 0

    for phrase in resized_batch:
        if np.array_equal(phrase, compare_phrase):
            count += 1

    return count / (resized_batch.shape[0] * resized_batch.shape[1])


def get_population_prob_dist(population, prev_word_array, review_batch):
    """
    Calculates the distribution of the probabilities of each word in the population
    occurring after the previous words that have been generated.

    :param population: Array of words that represents the individuals of a population
    :param prev_word_array: All of the previous words that have been generated
    :param review_batch: The batch of reviews that is being used to calculate the dist.
    :return: The probability distribution of the population
    """
    prob_dist = {}

    for individual in population:
        prob_dist[individual] = _prob_of_next_word(individual, prev_word_array, review_batch)

    return prob_dist


def get_expected_prob_dist(prev_word_array, review_batch):
    """
    Calculate the distribution of probabilities of all the unique words found in the review_batch
    occurring after the previously generated words.

    :param prev_word_array: Previously generated words
    :param review_batch: Batch of reviews used to calculate the distribution
    :return: Expected probability distribution found in the review batch
    """
    prob_dist = {}
    all_words = loader.get_words(review_batch)
    all_words_ = list(map(lambda x: len(x), all_words))
    sorted_words = all_words[np.argsort(all_words)]

    for i in range(0, len(sorted_words) - 1):
        if sorted_words[i + 1] == sorted_words[i]:
            np.delete(sorted_words, i)
        else:
            prob_dist[sorted_words[i]] = _prob_of_next_word(sorted_words[i],
                                                            prev_word_array, review_batch)

    return prob_dist


def calc_substring_freq_dist(population_dist, target_dist, substring_size):
    """
    Calculate the frequency distribution of random substrings taken from the
    population frequency distribution of size substring_size. The random substring
    frequency distribution is found by taking the probability of that substring occurring
    in the target frequency distribution.

    :param population_dist: A population probability distribution using get_population_prob_dist
    :param target_dist: The target distribution calculated with get_expected_prob_dist
    :param substring_size: Size of the substrings
    :return: The frequency distribution of random substrings from population_dist in target_dist
    """
    begin = 0
    end = substring_size - 1

    def get_comparison_substrings(substring_array, min_num_substrings=round(len(population_dist))):
        """
        Get random substrings of size substring_size from the substring_array.

        :param substring_array: Array that will hold substrings used for comparison
        :param min_num_substrings: The minimum number of substrings to get
        """
        for individual in population_dist:
            rand_index = random.randint(0, len(population_dist) - end)
            parent = individual[begin + rand_index:end + rand_index]
            np.append(substring_array, parent)

        substring_array = np.unique(substring_array)
        if len(substring_array) < min_num_substrings:
            get_comparison_substrings(substring_array, min_num_substrings)

    freq_dist = {}
    substring_array = np.array()
    freq = 0

    get_comparison_substrings(substring_array)
    for substring in substring_array:
        freq = len([m.start for m in re.finditer(substring, target_dist)])
        freq_dist[substring] = freq

    ordered_dict = collections.OrderedDict(sorted(freq_dist.items(), key=operator.itemgetter(1)))
    return ordered_dict



