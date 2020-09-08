import requests
from bs4 import BeautifulSoup


URL_base = 'https://nofluffjobs.com/pl/jobs/python?criteria=python&page='
intern_key_words = ["intern", "Intern", "Internship", "internship", "staz", "Staz", "Staż", "staż", "praktyka", "Praktyka"]
permanent_key_words = ["junior", "Junior"]
locations = ["Kraków", "kraków", "cracow", "Cracow", "Krakow", "krakow", "zdalna", "Zdalna"]

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
        name=job.find_all('div', class_="posting-title__wrapper")
        for n in name:
            title = n.find('h4')
            company=n.find('span')
            
            # turning the strings of job results to lists to search for my key words in them

        details =job.find_all('div', class_="posting-info position-relative d-none d-lg-flex flex-grow-1")
        for d in details:
            salary = d.find('span', class_="text-truncate badgy salary btn btn-outline-secondary btn-sm")
            region = d.find('span', class_="posting-info__location d-flex align-items-center ml-auto")
            technology = d.find('object')

            job = job.text  
            job = job.split()

            for word in permanent_key_words:
                for location in locations:
                    if word in job and location in region:
                        job=' '.join(job)
                    try:
                        print (title.text, company.text)
                    except AttributeError:
                        print (" No info")
                    try:
                        print (f' Salary: {salary.text}')
                    except AttributeError:
                        print (" Salary: No info")
                    try:
                        print (f' Technologies: {technology.text}')
                    except AttributeError:
                        print (" Technologies: No info")
                    try:
                        print (f' Region: {region.text}', end='\n'*2)
                    except AttributeError:
                        print (" Region: No info", end='\n'*2)
                    




            #looping through all my key words and selecting only <a> that have my key word
            for word in intern_key_words:
                if word in job:
                    job=' '.join(job)
                    try:
                        print (title.text, company.text)
                    except AttributeError:
                        print (" No info")
                    try:
                        print (f' Salary: {salary.text}')
                    except AttributeError:
                        print (" Salary: No info")
                    try:
                        print (f' Technologies: {technology.text}')
                    except AttributeError:
                        print (" Technologies: No info")
                    try:
                        print (f' Region: {region.text}', end='\n'*2)
                    except AttributeError:
                        print (" Region: No info", end='\n'*2)
                   
                
    #moving to the next result page        
    i=int(i)
    i+=1


