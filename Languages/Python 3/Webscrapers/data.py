from lxml import html
import requests
import bs4

# Requests API - Defining the data from the scrape + using beautifulsoup

response = requests.get('http://www.devbk.me')
response.content
response.text
# Status Code Loop
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not found!')

# Print (output)

print (response)
print (response.content)
print (response.text.title)
