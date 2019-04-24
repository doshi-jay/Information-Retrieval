#dictionary to store term, term frequency
d2 = {}                                                 
#gives the document ID for a particular document
docID = 0	
dir_ = "parsed/"											

url_crawled = []
# File to read all the links from
# This would help us in getting the names of the
# files stored in the dir_ directory
with open('BFS.txt','r') as f:
   l = f.readlines()

# Removing white spaces
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
    inv_index_bigram = {}
    global docID
    # Give each unique file a document Id
    docID += 1
    print docID
    # Generate the filename
    filename = dir_ + url.split('/')[-1] + ".txt"
    # Open file
    f = open(filename ,'r')
    # Read terms from the file
    terms = f.read()
    # Generating list of words 
    term_list = terms.split()
    # Get all the bigrams
    bigrams = generate_ngrams(term_list, 2)

    for term in bigrams:
        # Get the positions the term comes at
        positions = [i for i, x in enumerate(bigrams) if x == term]
        # Ignore if term is absent from the document
        if len(positions) == 0:
            continue
        else:
            # Set count of occurences in the dictionary
            d2[term] = len(positions)
        tuple = docID , len(positions)
        inv_index_bigram[term] = tuple

    return inv_index_bigram

parent_inverted_list = {}
for link in url_crawled:
    # Generate inverted_index for each link
    child_inverted_list = inverted_index(link)
    for term in child_inverted_list:

        if term in parent_inverted_list:
            #append the (docID,tf) for the term if the same term appears in another document
            parent_inverted_list[term].append(child_inverted_list[term])     
        else:
            parent_inverted_list[term] = [child_inverted_list[term]]

# Store the inverted bigram index list
output = open('inverted_list_bigram.txt', 'w')
for term in parent_inverted_list:
    # Write to the file
    output.write("%s -> %s\n" %(term , parent_inverted_list[term]))
output.close()
