import collections
import random
import numpy as np

from src import data_loader as loader
from src import data_proc as proc


"""Initial population state info"""
TRAINING_FILE = "Reviews.csv"

TRAINING_BATCHES = loader.read_reviews(TRAINING_FILE)
UNIQUE_TRAINING_INDIVIDUALS = [loader.get_all_words(batch) for batch in TRAINING_BATCHES]

MAX_INDIVIDUAL_SIZE = [len(batch_individuals) for batch_individuals in UNIQUE_TRAINING_INDIVIDUALS]


#possible put inside function
individuals = UNIQUE_TRAINING_INDIVIDUALS[random.randint(0, len(UNIQUE_TRAINING_INDIVIDUALS))]


NAMED_TUPLE_PARAMS = "training_batches, unique_training_individuals, max_individual_size, min_individual_size"
Population = collections.namedtuple("Populations", NAMED_TUPLE_PARAMS)



def train_model(training_file, mutation_rate):
    """
    Trains a genetic model using the fine food review data as training data.
    Individuals are randomly created, grouped into populations, analyzed for fitness, and
    the most fit individuals are randomly bred with each other with an unfit individual
    being randomly substituted at a rate equivalent to the mutation rate

    :param training_file: csv file that holds the training data
    :param mutation_rate: rate at which that parents are mutated during breeding
    :return: the genetic model data that has been cleaned and formatted
    """
    prev_word_array = np.array()
    init_pop = Population(training_batches=TRAINING_BATCHES,
                          unique_training_individuals=UNIQUE_TRAINING_INDIVIDUALS,
                          max_individual_size=MAX_INDIVIDUAL_SIZE,
                          min_individual_size=1)
    pop_dist = proc.get_population_prob_dist(init_pop.unique_training_individuals,
                                             prev_word_array, init_pop.training_batches)