#! python3
# searchpypi.py - Opens several search results.

import requests, sys, webbrowser, bs4
print('Searching...')  # display text while downloading the search result page
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result. NOTE LINKELEMS IS RETURNING 0
linkElems = soup.select('.package-snippet')
numOpen = min(5, len(linkElems))
if numOpen == 0:
    print('No links to search in new tab.')
else:
    for i in range(numOpen):
        urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
        print('Opening', urlToOpen)
        webbrowser.open(urlToOpen)
