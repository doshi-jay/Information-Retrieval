import requests
import re
from bs4 import BeautifulSoup

doclen = 0
docID_doclen = {}
url_crawled = []
with open('BFS.txt','r') as f:
   l = f.readlines()
l = [x.strip() for x in l]
url_crawled.extend(l)

dir_ = "parsed/"

def page_cleaner(url):                                               #Function for cleaning the page
    r = requests.get(url)
    page_content = r.text
    soup = BeautifulSoup(page_content,"html.parser")
    for link in soup("a"):
        href = str(link.get('href'))
        if href.startswith('#cite'):
            link.extract()                                            #remove citations
    for math in soup("script"):
        math.extract()                                                #extracts the javascript part
    for span in soup("span"):
        span.extract()                                                #extracts the mathematical formulae
    for req_content in soup.find_all("div",{"id":"bodyContent"}):
        req_content_text = req_content.text
        req_content_text = re.sub(r"[^0-9A-Za-z,-\.]"," ", req_content_text)   #retain alpha-numeric text along with ',' and '.'
        result_text = re.sub(r"(?!\d)[.,-](?!\d)"," ", req_content_text, 0)    #retain '.', '-' or ',' between digits
        filename = url.split('https://en.wikipedia.org/wiki/')[1]
        filename = filename + '.txt'
        result_text = result_text.split()
        for rt in result_text:                                        #remove minus and not hyphens
            if rt.startswith('-'):
                rt.replace(rt , rt.split('-')[1])
            if rt.endswith('-'):
                rt.replace(rt , rt.split('-')[0])
            else:
                continue
        result_text = ' '.join(result_text)
        f = open(dir_ + filename ,'w')
        result_text = result_text.lower()                             #convert everything to lower case
        f.write(result_text.strip())
        f.close()

for link in url_crawled:
    page_cleaner(link)												  #send each document present in the urlsCrawledBFS list for cleaning
