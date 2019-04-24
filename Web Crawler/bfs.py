import requests
from bs4 import BeautifulSoup
import time
import re


visited = []
frontier = []
max_links =1000
max_depth = 6

# words to be excluded from the url
excluded = ['mailto:', 'favicon', '.ico', ':',
            '.jpg', '.jpeg', '.png', '.gif', '#', '?',
            '.pdf', '.doc']

# file to store links executed in BFS 
filename = 'bfs.txt'
openfile = open(filename, 'w')


# Gets the desired URL and then crawls them in BFS order
# seed_factory stores the URL and it's current depth from the seed
def clean_and_crawl(seed_factory):

    # fetching url to be crawled
    seed = seed_factory[0]
    # fetching the depth
    depth = seed_factory[1]
    if depth > 6:
        return

    # politeness policy
    time.sleep(1)
    page = requests.get(seed)
    soup = BeautifulSoup(page.text, 'html.parser')
    download_files(soup, seed)

    # Getting links only from the content block and
    # not the links from the left margin and the footer.
    content = soup.find('div', {'id': 'mw-content-text'})

    # Getting only the links that start with /wiki
    for link in content.find_all('a', {'href': re.compile("^/wiki")}):

        # Ignoring the data in urls post #
        urls = link.get('href').split('#')[0]

        # If the fetched url is crawlable, only then move ahead
        if is_crawlable(link):
            urls = "https://en.wikipedia.org" + urls

            # Appending the url_pack to frontier
            frontier.append([urls, depth + 1])


# returns True if the given url is crawlable
def is_crawlable(link):

    urls = link.get('href').split('#')[0]

    # Ignoring images, files with ':' etc. Check excluded list.
    if not any(word in urls for word in excluded):

        # if we have not already crawled 1000 urls
        if len(visited) < max_links:

            # continue only if the given url is not visited
            if urls not in visited:

                # Ignoring page redirects
                classes = link.get('class')
                if (classes == None) or (not 'mw-redirect' in link.get('class')):
                    return True
    return False


# This is the main function that initiates the
# crawling of the urls in BFS order
def bfs(seed):
    print "In BFS"
    start = time.clock()
    frontier.append([seed, 1])

    # We keep updating the depth that we get from the url_pack
    depth = 0

    # continue till we have crawled max_links or frontier is not empty
    while len(visited) < max_links and len(frontier) > 0:
        current = frontier.pop(0)

        # Checking if depth is greater than 6
        if current[1] > 6:
            break

        # checking if node is not already visited
        if current[0] not in visited:
            #print len(visited)
            visited.append(current[0])

            # updating new depth
            depth = current[1]

            # adding the url to the file
            row = str(current[0]) + "\n"
            openfile.write(row)

            # crawling the next url
            clean_and_crawl(current)

    openfile.write("\nMax Depth: " + str(depth))
    openfile.close()
    print time.clock() - start


# downloading the files
def download_files(soup, url):
    fname = str(len(visited)) + ".txt"
    ofile = open(fname, 'w')
    print fname
    ofile.write("\n" + url + "\n")
    ofile.write(soup.get_text().encode('utf-8'))
    ofile.close()


seed = "https://en.wikipedia.org/wiki/Space_exploration"
bfs(seed)