import requests
from bs4 import BeautifulSoup

URL_base = 'https://nofluffjobs.com/pl/jobs/python?criteria=python&page='
my_key_words = ["intern", "Intern", "Internship", "internship", "staz", "Staz", "Staż", "staż", "praktyka", "Praktyka", "junior", "Junior"]

i=1

while i<15:
    i = str(i)
    url = URL_base + i
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    job_titles = soup.find_all('h4')
    for title in job_titles:
        title = title.text
        title = title.split()
        for word in my_key_words:
            if word in title:
                title=' '.join(title)
                print(title)
            
    i=int(i)
    i+=1


