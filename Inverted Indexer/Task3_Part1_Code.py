import pickle
import collections

with open("inverted_list_encoded.txt", 'rb') as f:
    inverted_index = pickle.loads(f.read())

with open("inverted_list_bigram_encoded.txt", 'rb') as f:
    inverted_index1 = pickle.loads(f.read())

with open("inverted_list_trigram_encoded.txt", 'rb') as f:
    inverted_index2 = pickle.loads(f.read())
	
''' sum of the term frequencies of a term occuring in it's respective document IDs 
    denotes the term frequency of that term for the whole given corpus '''

for term in inverted_index.keys():
    tf = sum([data[1] for data in inverted_index[term]])      
    inverted_index[term] = tf

for term in inverted_index1.keys():
    tf1 = sum([data[1] for data in inverted_index1[term]])
    inverted_index1[term] = tf1

for term in inverted_index2.keys():
    tf2 = sum([data[1] for data in inverted_index2[term]])
    inverted_index2[term] = tf2
	
#sort the dictionaries in descending order of term frequencies 

t_tf = collections.OrderedDict(sorted(inverted_index.items(), key = lambda s : s[1], reverse = True))
t_tf1 = collections.OrderedDict(sorted(inverted_index1.items(), key = lambda s : s[1], reverse = True))
t_tf2 = collections.OrderedDict(sorted(inverted_index2.items(), key = lambda s : s[1], reverse = True))

f = open('task3_part1_unigram.txt', 'w', encoding = 'utf-8')
for term in t_tf:
    f.write("term : %s , tf : %s\n" %(term , t_tf[term]))
f.close()

f = open('task3_part1_bigram.txt', 'w', encoding = 'utf-8')
for term in t_tf1:
    f.write("term : %s , tf : %s\n" %(term , t_tf1[term]))
f.close()

f = open('task3_part1_trigram.txt', 'w', encoding = 'utf-8')
for term in t_tf2:
    f.write("term : %s , tf : %s\n" %(term , t_tf2[term]))
f.close()
