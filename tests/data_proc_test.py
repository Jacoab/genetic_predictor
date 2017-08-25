from src import data_proc as proc
from src import data_loader as loader


reviews = loader.read_reviews("Reviews.csv")
reviews_word_batches = []

for batch in reviews:
    reviews_word_batches.append(loader.get_all_words(batch))

print(proc.get_population_prob_dist(reviews, ))

