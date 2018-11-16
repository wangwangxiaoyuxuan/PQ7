import nltk
from nltk.stem.lancaster import LancasterStemmer
import os
import json
import datetime
import csv
import numpy as np
import time
import re



def sigmoid_output_to_derivative(output):
    """Convert the sigmoid function's output to its derivative."""
    return output * (1-output)


def sigmoid(z):
    """
    returns the basic sigmoid formula for z. You can use
    numpy's exponential function exp() to do this.
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


def organize_raw_training_data(raw_training_data, stemmer):
    """
    1. Retrieve tokens from sentence (nltk.word_tokenize)
    2. Add list of tokens to list representing all words in set called "words"
    3. Add tokens with actor's name to list of docs called "docs"
    as tuple
    4. If new actor, add actor's name to list of classes (no duplicates, use set)
    """
    words = set()
    sentence_list = []
    for rtd_dict in raw_training_data:
        sentence_list.append(rtd_dict['sentence'])

    # Not sure how this function interacts with preprocess_words

    # for sentence in sentence_list:
    #     word_stem_list = preprocess_words(sentence, stemmer)
    #     words.append(word.tokenize(sentence))

    pass


def preprocess_words(words, stemmer):
    """ stem each word and returns a
    list of the word stems without duplicates.
    Strips words of punctuation
    ??? What about numbers?
    ??? Some regex confusion, try: preprocess_words(['investigating?', './.[investigating]', 'invest9igating', 'InvestIgatin9g'], stemmer)
    """
    word_stem_list = set()
    for raw_word in words:
        print("raw_word: ", raw_word)
        word = re.search('[A-Za-z]*', raw_word).group(0)
        print("word: ", word)
        word_stem = stemmer.stem(word)
        print("word_stem: ", word_stem)
        word_stem_list.add(word_stem)
    print(word_stem_list)
    return word_stem_list
    #pass


def get_raw_training_data(filename):
    """open a CSV file and extract its data into a
    dictionary structure. This dictionary will have
    two keys: "person", which is paired with the name
    of the actor who is speaking, and "sentence", which
    is paired with a sentence that person has said."""
    # right now can print properly, but something is terribly wrong with list
    rtd_dict_list = []
    rtd_dict = {'person': '', 'sentence': ''}
    with open('dialogue_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=('person', 'sentence'))
        for row in reader:
            print("What's in row -- ", row['person'], ": ", row['sentence'])
            rtd_dict['person'] = row['person']
            rtd_dict['sentence'] = row['sentence'].lower()
            print("What's rtd_dict -- ", rtd_dict)
            rtd_dict_list.append(rtd_dict)
            print(rtd_dict_list)
    return rtd_dict_list
    #pass


def main():
    stemmer = LancasterStemmer()
    raw_training_data = get_raw_training_data('dialogue_data.csv')
    # print(raw_training_data)

    # person_list = []
    # for rtd_dict in raw_training_data:
    #     sentence_list.append(rtd_dict['person'])

    # sentence_list = []
    # for rtd_dict in raw_training_data:
    #     sentence_list.append(rtd_dict['sentence'])

    # word_stem_list = preprocess_words(sentence_list, stemmer)
    preprocess_words(['investigating?', 'pot', 'investigation.'], stemmer)


    # words, classes, docs = organize_raw_training_data(raw_training_data, stemmer)


if __name__ == "__main__":
    main()
