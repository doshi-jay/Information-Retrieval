import urllib
from bs4 import BeautifulSoup
import re
from numpy import linalg as LA
import numpy as np
import operator

fname = "FOCUSED.txt"
dir_ = "souped/"

links = []
graph = dict()
sample_graph = dict()

with open(fname) as f:
    links = f.readlines()

print "Links length: " + str(len(set(links)))	


links = [link.strip() for link in links] 

stop_count = 0
lambda_ = 0.8
l2_norm = []
page_rank_sum = []

def get_difference(R, I):
	global saved_graph
	return [R[key] - I[key] for key in saved_graph.keys()]

def converged(vector):
	global stop_count
	global l2_norm

	norm = float(format(LA.norm(np.asarray(vector), 2), '.12g'))
	l2_norm.append(norm)

	if norm < 0.0005:
		if stop_count == 4:
			print "Yes"
			return True
		else:
			stop_count += 1
			print "No1"
			return False
	else:
		print "No2"
		return False

def pagerank(graph):
	global page_rank_sum

	R = dict()
	I = dict()

	for key in graph.keys():
		R[key] = 0
		I[key] = 1

	G = graph.keys()

	for i in range(len(I)):
		I[i] = 1.0/len(graph)

	change_rank = get_difference(R, I)
	t = 0
	while(not converged(change_rank)):
		t += 1
		for i in R.keys():
			R[i] = lambda_/len(graph)

		for p in graph.keys():
			Q = graph[p]

			if len(Q) > 0:
				for q in Q:
					R[q] = R[q] + ((1 - lambda_) * (I[p] / len(Q)))
			else:
				for q in graph.keys():
					R[q] = R[q] + ((1 - lambda_) * (I[p] / len(graph)))
	
	
			change_rank = get_difference(R, I)

			I = R
		page_rank_sum.append(sum(R.values()))

	return R


def build_graph():
	c = 0
	global max_links
	global links
	global graph
	global sources
	global sinks

	for curr_link in links:
		graph[curr_link] = []

	for curr_link in links:
		print c
		c += 1
		html = urllib.urlopen(curr_link).read()
		soup = BeautifulSoup(html, 'html.parser')
		content = soup.find('div', {'id': 'mw-content-text'})

		page_links = content.find_all('a', {'href': re.compile("^/wiki")})
		
		for link in page_links:
			link_ = "https://en.wikipedia.org" + link['href']
			
			if link_ in links:
				graph[curr_link].append(link_)

	np.save("focused-graph.npy", graph)
	

	


def build_sample_graph():
	global sample_graph
	sample_graph["A"] = ["B", "C", "F"]
	sample_graph["B"] = ["C", "D", "E", "F"]
	sample_graph["C"] = ["D", "E"]
	sample_graph["D"] = ["A", "C", "E", "F"] 
	sample_graph["E"] = ["A"]
	sample_graph["F"] = ["A", "B", "E"]	


build_graph()
# build_sample_graph()
saved_graph = np.load("focused-graph.npy").item()
R = pagerank(saved_graph)
R = sorted(R.items(), key = operator.itemgetter(1))
R.reverse()
np.save("pagerank-focused.npy", R)


print(l2_norm)
print(page_rank_sum)
for r in R[:25]:
	print(str(r) + "\n")
