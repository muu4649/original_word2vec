import numpy as np
import MeCab
import keras
import csv

def make_tokenize(text):
    m = MeCab.Tagger('-Owakati')
    return keras.preprocessing.text.text_to_word_sequence(m.parse(text))


def one_hot_dictionary(corpus):
    dictionary = []
    text = []
    for tokenize_text in corpus:
        tokenize_list = make_tokenize(tokenize_text)
        text.append(tokenize_list)
        for tokenize in tokenize_list:
            if not tokenize in dictionary:
                dictionary.append(tokenize)

    one_hot_dictionary = {}

    for text_one, corpus_text in zip(text, corpus):
        i = 0
        seq = np.zeros((len(text_one), len(dictionary)))
        for word in text_one:
            j = 0
            for dictionary_word in dictionary:
                if word == dictionary_word:
                    seq[i][j] +=1
                j += 1
            i += 1
        one_hot_dictionary[str(corpus_text)] = seq

    return one_hot_dictionary, len(dictionary)
csv_str='./word.csv'
text=csv.reader(csv_str.strip().splitlines())
print(one_hot_dictionary(text))
