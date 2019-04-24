import urllib
from bs4 import BeautifulSoup
import re

# File to get all links
fname = "BFS.txt"

links = []
graph = dict()

# Extract all links from the specified file
with open(fname) as f:
    links = f.readlines()

print "Links length: " + str(len(set(links)))	


# you may also want to remove whitespace characters like `\n` at the end of each line
links = [link.strip() for link in links] 
sinks = []
sources = []
max_links = 0


def store_graph():
	global graph

	# Open a file connection
	f = open("Task2-BFSGraph.txt", "w")

	# Write to the file
	for key in graph.keys():
		f.write(str(key) + "::" + str(graph[key]) + "\n\n")



def get_main_content():
	c = 0

	# Attach global variables to the local scope
	global max_links
	global links
	global graph
	global sources
	global sinks
	sinks = []

	# Initialize the list for each dictionary key
	for curr_link in links:
		graph[curr_link] = []

	for curr_link in links:
		print c
		c += 1
		# Extract the html content
		html = urllib.urlopen(curr_link).read()
		# Create a soup instance
		soup = BeautifulSoup(html, 'html.parser')
		# Get the main content
		content = soup.find('div', {'id': 'mw-content-text'})

		# Get all anchor tags as links which have wikipedia links as their href  
		page_links = content.find_all('a', {'href': re.compile("^/wiki")})
		
		# Only consider links which are in the file
		buffer_links = [] 
		for link in page_links:
			link_ = "https://en.wikipedia.org" + link['href']
			if link_ in links:
				buffer_links.append(link_)

		page_links = list(set(buffer_links))

		# Get sink pages
		if len(page_links) == 0:
			sinks.append(curr_link)

		# Find page with maximum in links
		if len(page_links) > max_links:
			max_links = len(page_links)
		
		# Create the graph
		for link in page_links:
			graph[link].append(curr_link)
		
get_main_content()
store_graph()


max_inlinks = 0
for key in graph:
	# Find page with minimum in links
	if len(graph[key]) > max_inlinks:
		max_inlinks = len(graph[key])

	# Get source pages
	if len(graph[key]) == 0:
		sources.append(key)

print "==========SOURCES========="
print sources
print "==========SINKS========="
print sinks
print "==========MAX_OUT_LINKS========="
print max_links
print "==========MAX_IN_LINKS========="
print max_inlinks

