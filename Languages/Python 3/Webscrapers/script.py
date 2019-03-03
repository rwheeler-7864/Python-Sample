from lxml import html
import requests

# Define ()

#requests = ('requests')
#response = ('response')
#status_code = ('status_code')
#url = ('http://www.devbk.me')
#data = ('page')


# Data want to pull from script.

title = ('title')                               # Title of page
h1 = ('h1')                                     # Heading 1 of articles
print(title + h1)

# Requests API

response = requests.get('http://www.devbk.me')
response.content
response.text
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not found!')

print (response)
print (response.content)
print (response.text)