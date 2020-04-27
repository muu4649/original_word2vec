import nltk
nltk.download('punkt')
string = "I AM A CAT. As yet I have no name."
words = nltk.word_tokenize(string)
print(type(words))
