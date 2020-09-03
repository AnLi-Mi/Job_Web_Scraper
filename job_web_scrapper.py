import requests

URL = 'https://justjoin.it/krakow/python/junior'
page = requests.get(URL)
print (page.text)
