import urllib
from bs4 import BeautifulSoup
from nltk.util import ngrams

# Global parameters that can be edited
fname = "BFS.txt"
dir_ = "souped/"
lower = True
remove_punctuations = True

links = []

# Read all links from the given file
with open(fname) as f:
    links = f.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
links = [link.strip() for link in links] 

def get_main_content():
	global links

	# Iterate over all links in the given file
	for link in links: 
		print "Parsing link: " + link
		
		# Read URL and get the html content 
		html = urllib.urlopen(link).read()
		# Make a soup object
		soup = BeautifulSoup(html)
		# Get the title to store as filename
		title = soup('title')[0].text

		# Split titles which have complex path structure
		if (len(title.split("/")) > 1):
			print title
			title = title.split("/")[1]


		# kill all script and style elements
		for script in soup(["script", "style"]):
			script.extract()    # rip it out

		# get main text
		soup.find('div', {'id': 'mw-content-text'})

		text = soup.get_text()

		# break into lines and remove leading and trailing space on each
		lines = (line.strip() for line in text.splitlines())
		# break multi-headlines into a line each
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		# drop blank lines

		if remove_punctuations:
		# Removing the punctuations except hiphens
			text = '\n'.join(chunk for chunk in chunks if chunk).replace(",", "").replace("?", "").replace("!", "").replace(":", "")
		else:
			text = '\n'.join(chunk for chunk in chunks if chunk)

		# Make text lower if specified
		if lower:
			text = text.lower()

		# Write to the file
		f = open(dir_ + title + ".txt", "w")
		f.write(text.encode('utf-8'))
