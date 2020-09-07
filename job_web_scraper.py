import requests
from bs4 import BeautifulSoup


URL_base = 'https://nofluffjobs.com/pl/jobs/python?criteria=python&page='
my_key_words = ["intern", "Intern", "Internship", "internship", "staz", "Staz", "Staż", "staż", "praktyka", "Praktyka", "junior", "Junior"]

i=1


while i<15:
    # looping through multiple pages of results
    i = str(i)
    url = URL_base + i
    #scraping results for each page
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #filtering only job titles which are all h4
    jobs = soup.find_all('a')
    # turning the strings of job titles to lists to search for my key words in them
    for job in jobs:
        job = job.text
        job = job.split()
        #looping through all my key words
        for word in my_key_words:
            if word in job:
                job=' '.join(job)
                print(job)
    #moving to the next result page        
    i=int(i)
    i+=1


