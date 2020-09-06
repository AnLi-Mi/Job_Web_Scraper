import requests
from bs4 import BeautifulSoup

URL = 'https://nofluffjobs.com/pl/jobs/krakow?criteria=city%3Dkrakow&page=1'
page = requests.get(URL)

my_key_words = ["intern", "internship", "staz", "staż", "praktyka"]

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup)

job_titles = soup.find_all('h4')

for word in my_key_words:
    for title in job_titles:
        title = title.text
        title = title.split()
        if word in title:
            title=' '.join(title)
            print(title)
       
