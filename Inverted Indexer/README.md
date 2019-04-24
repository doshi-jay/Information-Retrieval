## Dependencies
The system expects parsed text files in the directory `parsed` that must be created 
## Task 1: 
### Implement an inverted indexer and create inverted indexes

#### Files:
- `creating_unigram_inverted_list.py`
- `creating_bigram_inverted_list.py`
- `creating_trigram_inverted_list.py`


The code uses python dictionary to store the index data. The generated unigram, bigram, and trigram indexes are written into files:

- `inverted_list_unigram.txt`
- `inverted_list_bigram.txt`
- `inverted_list_trigram.txt`

For creating positional inverted indexes there are two python files:
- `creating_positional_unigram_inverted_list.py` - creates a positional index for unigram
- `creating_positional_unigram_inverted_list_delta.py` - creates delta encoded unigram positional inverted list

The delta encoded inverted list of unigrams is created and stored in `inverted_list_unigram_delta_encoding.txt`


## Task 2: 
### Use Positional Index to Process Conjunctive Proximity Queries

Using the positional inverted index from the above section, retrieving a list of documents that contain pair of terms within a proximity of k.

- `pair_of_words_within_window.py`


## Task 3: 
### Compute Corpus Statistics; Propose Stop Lists

* #### Part 1
    * Generate a term frequency table comprising of two
columns: term and term frequency (for the corpus).
    * Sort the table from most to least frequent.

* #### Part 2
    * Generate a document frequency table comprising of three columns: term, docIDs, and document frequency. 
    * Sort lexicographically based on term.
* #### Part 3:
    * Generate 3 stop lists, one per index from Task 1.

#### Files:
- `stop_list_generation_unigram.py`
- `stop_list_generation_bigram.py`
- `stop_list_generation_trigram.py`

Contains the code stop list generation 
