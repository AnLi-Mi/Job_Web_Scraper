import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

def jobs_fetch(url):
    #scraping results for each page
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #filtering only elementswhich are <a> - like clickable job offer 
    jobs = soup.find_all('a')
    return jobs

def permanent_jobs_krk_fetch(job):   

    global region
    global title
    global salary
    global company
    global technologies
    
    permanent_key_words = ["junior", "Junior"]
    locations = ["Kraków,", "kraków,", "cracow,", "Cracow,", "Krakow,", "krakow,", "zdalna,", "Zdalna,", "zdalna", "Zdalna"]
                          
    for word in permanent_key_words:        
        if word in job:
            for location in locations:                                             
                if location in region:                                
                    job=' '.join(job)
                    region=' '.join(region)
                    print("Type: PERMANENT JOBS IN KRAKOW:")
                    try:
                        print (f' Position: {title.text.strip()}')
                    except AttributeError:
                        print (" Position: No info")
                    try:
                        print (f' Company: {company.text.strip()}')
                    except AttributeError:
                        print (" Company: No info")
                    try:
                        print (f' Salary: {salary.text.strip()}')
                    except AttributeError:
                        print (" Salary: No info")
                    try:                                 
                        print (f' Technologies: {technology.text.strip()}')
                    except AttributeError:
                        print (" Technologies: No info")
                    try:
                        print (f' Region: {region}', end='\n'*3)
                    except AttributeError:
                        print (" Region: No info", end='\n'*3)


def internships_anywhere_fetch(job):

    global region
    global title
    global salary
    global company
    global technologies
     
    intern_key_words = ["intern", "Intern", "Internship", "internship", "staz", "Staz", "Staż", "staż", "praktyka", "Praktyka"]
    
    #looping through the ad's list of words to find a my key words for Intern position
    for word in intern_key_words:
        if word in job:            
            # joining the job and region into string again so it dispaly better in 'print'
            job=' '.join(job)
            print("Type: INTERNSHIPS ANYWHERE:")
            # printing the details of the filtered ads
            try:
                print (f' Position: {title.text}')
            except AttributeError:
                print (" Position: No info")
            try:
                print (f' Company: {company.text}')
            except AttributeError:
                print (" Company: No info")
            try:
                print (f' Salary: {salary.text}')
            except AttributeError:
                print (" Salary: No info")
            try:
                print (f' Technologies: {technology.text}')
            except AttributeError:
                print (" Technologies: No info")
            try:
                print (f' Region: {"".join(region)}', end='\n'*2)
            except AttributeError:
                print (" Region: No info", end='\n'*2)
                                                      

def no_fluffjobs(number_of_pages):

    i=1
    while i<number_of_pages + 1:
        i = str(i)
        url = 'https://nofluffjobs.com/pl/jobs/python?criteria=python&page=' + i

        jobs = jobs_fetch(url)

        for job in jobs:   
                        
            # scraping ad's main information from first 'div' element
            name=job.find_all('div', class_="posting-title__wrapper")
            for n in name:
                global title
                title = n.find('h4')
                global company
                company=n.find('span')
                #return title, company
                
                                    
            #scraping ad's more specific details from second 'div' element
            details =job.find_all('div', class_="posting-info position-relative d-none d-lg-flex flex-grow-1")
            for d in details:
                global salary
                salary = d.find('span', class_="text-truncate badgy salary btn btn-outline-secondary btn-sm")
                global technology
                technology = d.find('object')
                global region
                region = d.find('span', class_="posting-info__location d-flex align-items-center ml-auto")
                # spliting the scrped region into a list so I can loop through its individual words later
                region = region.text
                region= region.split()
                #return salary, technology, region
                                                    
                # spliting the scrped job ad into a list so I can loop through its individual words later
            job = job.text  
            job = job.split()
            #global region
            #print(f'Region: {region}')

            
            internships_anywhere_fetch(job)
            permanent_jobs_krk_fetch(job)

        i=int(i)
        i+=1



no_fluffjobs(18)
