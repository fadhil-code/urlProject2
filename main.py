
text_file = open("Natural_Language_Processing_Text.txt")

#Read the data :
text = text_file.read()

#Datatype of the data read :
print (type(text))
print("\n")

#Print the text :
print(text)
print("\n")
#Length of the text :
print (len(text))

import nltk
from nltk import sent_tokenize
from nltk import word_tokenize

#Tokenize the text by sentences :
sentences = sent_tokenize(text)

#How many sentences are there? :
print ( len(sentences))

#Print the sentences :
print(sentences)

#Tokenize the text with words :
words = word_tokenize(text)

#How many words are there? :
print (len(words))
print("\n")

#Print words :
print (words)

from nltk.probability import FreqDist

#Find the frequency :
fdist = FreqDist(words)

#Print 10 most common words :
fdist.most_common(10)

#Plot the graph for fdist :
import matplotlib.pyplot as plt

fdist.plot(10)

#Empty list to store words:
words_no_punc = []

#Removing punctuation marks :
for w in words:
    if w.isalpha():
        words_no_punc.append(w.lower())

#Print the words without punctution marks :
print (words_no_punc)

print ("\n")

#Length :
print (len(words_no_punc))

#Frequency distribution :
fdist = FreqDist(words_no_punc)

fdist.most_common(10)


#Plot the most common words on grpah:

fdist.plot(10)
