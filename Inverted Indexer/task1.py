import urllib
from bs4 import BeautifulSoup
from nltk.util import ngrams
import re

# Global parameters that can be edited
fname = "BFS.txt"
dir_ = "parsed/"
lower = True
remove_punctuations = True

links = []

# Read all links from the given file
with open(fname) as f:
    links = f.readlines()
print len(links)
# you may also want to remove whitespace characters like `\n` at the end of each line
links = [link.strip() for link in links] 

count = 0
def get_main_content():
	global links
	global count



	# Iterate over all links in the given file
	for link in links: 
		count += 1
		print count
		print "Parsing link: " + link
		
		# Read URL and get the html content 
		html = urllib.urlopen(link).read()
		# Make a soup object
		soup = BeautifulSoup(html)

		# kill all script and style elements
		for script in soup(["script", "style", "span"]):
			script.extract()

		# get main text
		for req_content in soup.find_all("div",{"id":"bodyContent"}):
			req_content_text = req_content.text
			#retain alpha-numeric text along with ',' and '.'
			req_content_text = re.sub(r"[^0-9A-Za-z,-\.]"," ", req_content_text)   
			result_text = re.sub(r"(?!\d)[.,-](?!\d)"," ", req_content_text, 0) 
			filename = link.split('/')[-1]
			filename = filename + '.txt'
			result_text = result_text.split()
			#remove minus and not hyphens
			for rt in result_text:                                        
				if rt.startswith('-'):
					rt.replace(rt , rt.split('-')[1])
				if rt.endswith('-'):
					rt.replace(rt , rt.split('-')[0])
				else:
					continue

		result_text = str(' '.join(result_text))
		f = open(dir_ + filename ,'w')
		# Make lower the result_text to ensure case has no effect
		result_text = result_text.lower()
		# Write to the file
		f.write(result_text.encode('utf-8'))
		# Close the connection
		f.close()
		

get_main_content()