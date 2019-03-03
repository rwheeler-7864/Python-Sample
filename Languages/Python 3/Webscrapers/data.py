import requests
import bs4
import BeautifulSoup
from lxml import html

# Requests API - Defining the data from the scrape + using beautifulsoup

soup = BeautifulSoup('<a href''> </a>')

response = requests.get('http://www.devbk.me')
response.content
response.text
# Status Code Loop
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not found!')

soup.title
soup.find_all('a')

# Print (output)

print (response)
print (response.content)
print (response.text.title)

# Export Data to export.txt (locally)