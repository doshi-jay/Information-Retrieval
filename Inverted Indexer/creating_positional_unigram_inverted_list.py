import collections

#dictionary to store term, term frequency 
d1 = {}                                                      
#gives the document ID for a particular document
docID = 0                                                    
#list to store all the document names obtained
doc_name = []                                                
#dictionary to store the document length of a particular document
docID_doclen = {}                                            

docID_docName = {}

dir_ = "parsed/"

url_crawled = []
# File to read all the links from
# This would help us in getting the names of the
# files stored in the dir_ directory
with open('BFS.txt','r') as f:
    l = f.readlines()
l = [x.strip() for x in l]
url_crawled.extend(l)

#Function to generate n-grams
def generate_ngrams(words_list, n):                           
    ngrams_list = []
    for num in range(0, len(words_list)):
        ngram = ' '.join(words_list[num:num + n])
        ngrams_list.append(ngram)

    return ngrams_list

#Function to generate inverted index
def inverted_index(url):                                     
    inv_index_unigram = {}
    global docID, doc_name
    # Give each unique file a document Id
    docID += 1
    print docID
     # Generate the filename
    filename = url.split('/')[-1]
    doc_name.append(filename)
    docID_docName[docID] = doc_name
    filename = dir_ + filename + '.txt'
    # Open file
    f = open(filename ,'r')
    # Read terms from the file
    terms = f.read()
    # Generating list of words 
    term_list = terms.split()
    docID_doclen[docID] = len(term_list)
    index = 0
    positions = []
    for term in term_list:
         # Get the positions the term comes at
        positions = [i for i, x in enumerate(term_list) if x == term]
         # Ignore if term is absent from the document
        if len(positions) == 0:
            continue
         # Set count of occurences in the tuple
        tuple = docID , len(positions), positions
        inv_index_unigram[term] = tuple
        index += 1
    return inv_index_unigram

parent_inverted_list = {}
for link in url_crawled:
    child_inverted_list = inverted_index(link)
    for term in child_inverted_list:
        if term in parent_inverted_list:
            #append the (docID,tf, pos) for the term if the same term appears in another document
            parent_inverted_list[term].append(child_inverted_list[term])              
        else:
            parent_inverted_list[term] = [child_inverted_list[term]]

#sort the inverted index
inv_list_unigram = collections.OrderedDict(sorted(parent_inverted_list.items()))      

output = open('inverted_list_unigram.txt', 'w+')
for term in inv_list_unigram:
    # Write to the file
    output.write("%s -> %s\n" %(term , inv_list_unigram[term]))
output.close()

#File to show document ID to document Name mapping
f = open("DocumentIDs.txt", 'w')

for i in range (0,len(url_crawled)):
    # Write to the file
    f.write("Document ID : %d Document Name : " %(i+1))
    f.write(doc_name[i] + "\n")
f.close()

f = open("DocumentID-DocLen.txt", 'w')
# Write to the file
f.write(str(docID_doclen))
f.close()


