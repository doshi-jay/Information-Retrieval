import requests
from bs4 import BeautifulSoup
import time
import re
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet


visited = []
frontier = []
max_links =1000
max_depth = 6
revisit_count = 0

# words to be excluded from the url
excluded = ['mailto:', 'favicon', '.ico', ':',
            '.jpg', '.jpeg', '.png', '.gif', '#', '?',
            '.pdf', '.doc']

# words that need to be included in the url for focussed crawling
included = ["spaceflights", "launch", "mars","rover", "orbiter", "pathfinder", "mars mission", "mars exploration", "mission", "exploration", "space", "astronauts", "astronaut", "rocket", "flight"]

# opening the file to write the urls
filename = 'focused.txt'
openfile = open(filename, 'w')

# This function first gets the desired urls and then crawls them in BFS order
# seed_factory stores the URL and it's current depth from the seed
def clean_and_crawl(seed_factory):

    # fetching url to be crawled
    seed = seed_factory[0]

    # fetching the depth
    depth = seed_factory[1]

    if depth > 6:
        return

    # politeness policy
    # time.sleep(1)
    page = requests.get(seed)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Getting links only from the content block and
    # not the links from the left margin and the footer.
    content = soup.find('div', {'id': 'mw-content-text'})

    # Getting only the links that start with /wiki
    for link in content.find_all('a', {'href': re.compile("^/wiki")}):

        # Ignoring the data in urls post #
        urls = link.get('href').split('#')[0]
        anchor = ''

        # Continue only if the fetched url is crawlable
        if is_crawlable(link):
            urls = "https://en.wikipedia.org" + urls
            #print [urls, depth + 1, seed]

            #append it to frontier
            frontier.append([urls, depth + 1])


# returns True if the given url is crawlable
def is_crawlable(link):
    global revisit_count
    url = link.get('href').split('#')[0]

    # anchor text of the url
    anchor = ''

    # Ignoring images, files with ':' etc. Check excluded list.
    if not any(word in url for word in excluded):

        # if we have not already crawled 1000 urls
        if len(visited) < max_links:

            # getting the anchor text for the url
            try:
                anchor = str(link.text)
            except UnicodeEncodeError as e:
                pass


            # continue only if the given url is not visited
            if url not in visited:
                # Ignoring page redirects
                classes = link.get('class')
                if (classes == None) or (not 'mw-redirect' in link.get('class')):

                    # check if the given url is focused
                    if check_if_focused(url, anchor):
                        return True
            else:
                revisit_count += 1
    return False


# returns true if the given url is a focused url
def check_if_focused(url, anchor):

    # fetching the anchor text and url
    url = url.lower()
    anchor = anchor.lower()

    for keyword in included:

        # if the keyword is present in the url or the anchor, continue
        if keyword in url or keyword in anchor:

            # breaking the anchor and url into an array of words
            url_words = url[6:].replace("-", "_").split("_")
            anchor_words = anchor.split(" ")

            for u_w in url_words:
                if keyword in u_w:

                    # removing brackets and removing the keyword
                    check = u_w.replace(keyword, '').strip("(){}[]-")

                    # after removing the keyword, if the rest of the word is
                    # a valid word, return True
                    if check == '':
                        return True
                    if wordnet.synsets(check):
                        return True
            for u_w in anchor_words:
                if keyword in u_w:
                    # removing brackets and removing the keyword
                    check = u_w.replace(keyword, '').strip("(){}[]-")

                    # after removing the keyword, if the rest of the word is
                    # a valid word, return True
                    if check == '':
                        return True
                    if wordnet.synsets(check):
                        return True
    return False



def bfs(seed):

    frontier.append([seed, 1, 'none'])
    depth = 0
    while len(visited) < max_links and len(frontier) > 0:
        current = frontier.pop(0)
        if current[1] > 6:
            break
        if current[0] not in visited:
            #print len(visited)
            visited.append(current[0])
            depth = current[1]
            row = str(current[0]) + "\n"
            openfile.write(row)
            # print current
            clean_and_crawl(current)

    openfile.write("\n depth: " + str(depth))
    openfile.close()




seed = "https://en.wikipedia.org/wiki/Space_exploration"
# start([seed, 0])
bfs(seed)
print "Revisited Count" + str(revisit_count)