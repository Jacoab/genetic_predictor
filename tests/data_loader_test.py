#
# Programmed By: Jake Jongewaard
#
# Unit test for the utilities provided in the data_loader.py file
#===================================================================


from src import data_loader as loader


REVIEW_FILE = "Reviews.csv"


print("Beginning unit tests of data_loader.py...")

""" read_reviews(filename) test """
print(loader.read_reviews(REVIEW_FILE)[4][4])