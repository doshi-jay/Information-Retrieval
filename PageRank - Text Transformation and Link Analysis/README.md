## System Requirements

For running the files, we would need the following libraries: 

1. Python (>= v 2.7)

2. BeautifulSoup     - pip install --upgrade --force-reinstall beautifulsoup4 

3. NLTK              - http://www.nltk.org/install.html

4. Matplotlib        - pip install matplotlib


## Task 1: Tokenizing and creating trigrams

- task1.py : Does Task 1-a. Downloads all articles in BFS.txt
- task1-trigrams.py : Does the remaining part of Task 1. 
	All the trigrams can be found in Trigrams.txt
	The plot image can be found in Task1-Trigram-Plot.png

- Task1-Deliverables.txt : This file contains the answers to the analysis part in Task1 


## Task 2: Constructing directed web graphs

- task2-bfs.py : This file does Task 2-a. It generates inlink graph for links in BFS.txt
- task2-focused.py : This file does Task 2-b. It generates inlink graph for links in FOCUSED.txt 
- Task 2.txt : This file contains a brief report on simple statistics for G1 and G2 such as the sources, sink, max in degree, max out degree.
- Task2-BFSGraph.txt : This file contains grpah for BFS.txt
- Task2-FOCUSEDGraph.txt : This file contains grpah for FOCUSED.txt


## Task 3: Link analysis: PageRank Implementation

- pagerank.py : This file contains the implementation of page rank as mentioned in the textbook for BFS.txt
- pagerank-focused.py : This file contains the implementation of page rank as mentioned in the textbook for FOCUSED.txt
- Task3-BFS-Deliverables : This file contains the L2 Norm values, Page rank sums and the top 50 links for G1
- Task3-FOCUSED-Deliverables : This file contains the L2 Norm values, Page rank sums and the top 50 links for G2

## Task 4: Experiments with PageRank

- Task 4.txt : This file answers questions pertaining to task 4


