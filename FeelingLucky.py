#! python3
#FeelingLucky.py - Opens Several Google search results in different tabs of browser

import requests, bs4, webbrowser, sys

print('Goooogggglinggggg...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))

try:
    res.raise_for_status()
except Exception as exc:
    print('There is a problem: %s' % (exc))

soup = bs4.BeautifulSoup(res.text, 'html.parser')

linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))

for i in range(numOpen):
     webbrowser.open('http://google.com' + linkElems[i].get('href'))
