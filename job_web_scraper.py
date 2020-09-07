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
    #filtering only elementswhich are <a> - like clickable job offer 
    jobs = soup.find_all('a')

    #looping theough the results of <a> elements
    for job in jobs:
        # scraping specific job information
        details=job.find_all('div', class_="posting-title__wrapper")
        for d in details:
            title = d.find('h4')
            company=d.find('span')
            #salary = details.find ('div class="posting-info position-relative d-none d-lg-flex flex-grow-1"')
            # turning the strings of job results to lists to search for my key words in them
            job = job.text  
            job = job.split()
            #looping through all my key words and selecting only <a> that have my key word
            for word in my_key_words:
                if word in job:
                    job=' '.join(job)
                    print (title.text, company.text, end='\n'*2)
                   # print (region)
                   
    #moving to the next result page        
    i=int(i)
    i+=1


