import requests
from bs4 import BeautifulSoup

URL = 'https://justjoin.it/krakow/python/junior'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup)

results = soup.find('title')
print(results)
