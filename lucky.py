#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import sys
import webbrowser
import bs4

print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

linkElements = soup.select('r.a')
numOpen = min(5, len(linkElements))
for i in range(numOpen):
    webbrowser.open('http://google.com/' + linkElements[i].get('href'))
