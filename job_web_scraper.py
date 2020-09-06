import requests
from bs4 import BeautifulSoup

URL = 'https://nofluffjobs.com/pl/jobs/krakow?criteria=city%3Dkrakow&page=1'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup)

job_titles = soup.find_all('h4')

for title in job_titles:
    title = title.text
    title = title.split()
    if "internship" in title or "intern" in title:
        title=' '.join(title)
        print(title)
       
