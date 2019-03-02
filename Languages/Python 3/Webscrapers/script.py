import requests
from lxml import html


# request data (request page)

page = requests.get('http://devbk.me')
tree = html.fromstring(page.content)


# print out soup
print(tree)





