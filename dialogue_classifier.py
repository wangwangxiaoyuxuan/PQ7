import nltk
from nltk.stem.lancaster import LancasterStemmer
import os
import json
import datetime
import csv
import numpy as np
import time




if __name__ == "__main__":
    main()

def main():
    stemmer = LancasterStemmer()
    raw_training_data = get_raw_training_data('dialogue_data.csv')

    words, classes, docs = organize_raw_training_data(raw_training_data, stemmer)



def get_raw_training_data(filename):
    """open a CSV file and extract its data into a 
    dictionary structure. This dictionary will have 
    two keys: "person", which is paired with the name 
    of the actor who is speaking, and "sentence", which 
    is paired with a sentence that person has said."""
    pass

def preprocess_words(words, stemmer):
    """ stem each word and returns a 
    list of the word stems without duplicates.
    Strips words of punctuation
    """
    pass

def organize_raw_training_data(raw_training_data, stemmer):
    """
    1. Retrieve tokens from sentence (nltk.word_tokenize)
    2. Add list of tokens to list representing all words in set called "words"
    3. Add tokens with actor's name to list of docs called "docs" 
    as tuple
    4. If new actor, add actor's name to list of classes (no duplicates, use set)
    """

    pass

def create_training_data(word_stems, classes, docs, stemmer):
    """
    Purpose: training_data variable, you will need to create a bag 
            of words for each sentence as represented in your documents. 
            Append each of these bags to the training_data variable.
    Outputs: training_data = list of bag of word correlations, 
            output is list of sentences by who has said them before

    """

    pass

def sigmoid(z):
    """
    returns the basic sigmoid formula for z. You can use 
    numpy's exponential function exp() to do this.
    """
    pass

def sigmoid_output_to_derivative(output):
    """Convert the sigmoid function's output to its derivative."""
    return output * (1-output)


