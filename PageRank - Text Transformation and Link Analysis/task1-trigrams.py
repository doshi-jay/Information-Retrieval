import glob   
import urllib
import operator
from bs4 import BeautifulSoup
import math
from nltk.util import ngrams
from nltk.corpus import stopwords 
import nltk
from numpy import median
import matplotlib.pyplot as plt
nltk.download('punkt')
nltk.download('stopwords')


dir_ = "souped/"

trigrams_frequency = dict()

stop_words = set(stopwords.words('english'))

words = set()

path = dir_ + "*.txt"   
files = glob.glob(path)   
for file in files:     
	f = open(file, 'r')  
	lines = f.readlines()
	for line in lines:
		line = line.lower()
		for word in line.split(" "):
			if word not in stop_words:
				word = word.strip()
				words.add(word)

	#Create your bigrams
	bgs = nltk.trigrams(words)
	for trigram in bgs:
		if trigram in trigrams_frequency:
			trigrams_frequency[trigram] += 1
		else:
			trigrams_frequency[trigram] = 1
	words = set()

sorted_trigrams = sorted(trigrams_frequency.items(), key = operator.itemgetter(1))
sorted_trigrams.reverse()

with open("Trigrams.txt", 'w') as f:
    for trigram in sorted_trigrams:
        f.write("\n" + str(trigram))

frequencies = [math.log(math.log(i[1])) for i in sorted_trigrams[:20000]]
ranks = [i+1 for i in range(len(frequencies))]

total = []
for i in range(len(frequencies)):
	total.append((frequencies[i]/len(frequencies))*ranks[i])

print median(sorted(total))

plt.plot(ranks, frequencies)
plt.xlabel("Ranks")
plt.ylabel("Log Log Frequencies")
plt.show()


