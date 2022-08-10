from types import NoneType
import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup #this pulls through everything needed from beautiful soup\

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser') #This is the line that tells beautiful soup to make the page readable

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
