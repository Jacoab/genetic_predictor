import random

from src import data_loader as loader

"""Initial population state info"""
TRAINING_FILE = "Reviews.csv"

TRAINING_BATCHES = loader.read_reviews(TRAINING_FILE)
UNIQUE_TRAINING_INDIVIDUALS = [loader.get_all_words(batch) for batch in TRAINING_BATCHES]

MAX_INDIVIDUAL_SIZE = [len(batch_individuals) for batch_individuals in UNIQUE_TRAINING_INDIVIDUALS]


#possible put inside function
individuals = UNIQUE_TRAINING_INDIVIDUALS[random.randint(0, len(UNIQUE_TRAINING_INDIVIDUALS))]


def _initialize_population(training_batches, unique_training_individuals, max_individual_size,
                           min_individual_size=1):
    class Population(object):
        pass

    pop = Population()
    pop.training_batches = training_batches
    pop.unique_training_individuals = unique_training_individuals
    pop.max_individual_size = max_individual_size
    pop.min_individual_size = min_individual_size

    return pop


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
    init_pop = _initialize_population(TRAINING_BATCHES, UNIQUE_TRAINING_INDIVIDUALS, MAX_INDIVIDUAL_SIZE)
