import requests
from lxml import html
from bs4 import BeautifulSoup


# Get the webpage
r = requests.get, ('http://devbk.me')                         #fine!!

# Making the soup


markup = html
soup = 	BeautifulSoup(markup, "html.parser")
len(soup)

print(soup)