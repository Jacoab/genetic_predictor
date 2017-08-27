from src import data_proc as proc
from src import data_loader as loader


review_batches = loader.read_reviews("Reviews.csv")
test_set = review_batches[2]
test_set_words = loader.get_words(test_set, 10)

# for review in test_set:
#     print(proc.get_population_prob_dist(test)

