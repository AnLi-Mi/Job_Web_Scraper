import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession



# using beutifullsoup to fatch all <a> elements from the site (as job ads are posted as <a> elements)
def jobs_fetch(url):
            
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    jobs = soup.find_all('a')
    return jobs

     
# filtring permanent jobs in specific region looping through the <a> alements' content to find key words
def permanent_jobs_krk_fetch(job):

    # calling global variables defined in other function to use them further in ths function 
    global region
    global title
    global salary
    global company
    global technologies
    
    #preparing lists of my key words defining job title and later a region/location of the job
    permanent_key_words = ["junior", "Junior"]
    locations = ["Kraków,", "kraków,", "cracow,", "Cracow,", "Krakow,", "krakow,", "zdalna,", "Zdalna,", "zdalna", "Zdalna"]
                                                    

    for word in permanent_key_words:
        if word in job:
            for location in locations:                                            
                if location in region:
                    # turn the splited job and region variables (for puspose of looping through them) back to strings again
                    job=' '.join(job)
                    region=' '.join(region)
                    print("Type: PERMANENT IN KRAKOW")
                    # printing neatly all filtered job's details
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


# filtring intership jobs looping through the <a> alements' content to find key words                               
def internships_anywhere_fetch(job):
    
    # calling global variables defined in other function to use them further in ths function 
    global region
    global title
    global salary
    global company
    global technologies
    
    #preparing lists of my key words defining intership job title 
    intern_key_words = ["intern", "Intern", "Internship", "internship", "staz", "Staz", "Staż", "staż", "praktyka", "Praktyka"]  
                    
    #looping through the ad's list of words to find a my key words for Intern position
    for word in intern_key_words:
        if word in job:
            # turn the splited job variable (for puspose of looping through them) back to strings again
            job=' '.join(job)
            print("Type: INTERNSHIPS ANYWHERE")
            
            # printing neatly all filtered job's details
            try:
                t = title.text
                print (f' Position: {t}')
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
            return job
            
                        
                       
# scraping process specific for the NoFluffJobs site's structure          
def no_fluffjobs(number_of_pages):

    print ('------------------- NO FLUFF JOBS -------------------', end='\n'*2)
    i=1

    while i<number_of_pages +1:
        # looping through indicated nuber of pages with job ads results 
        i = str(i)
        url = 'https://nofluffjobs.com/pl/jobs/python?criteria=python&page=' + i

        # using the function to fetch all <a> elements
        jobs=jobs_fetch(url)

        #looping through all <a> elements
        for job in jobs:                   
            
            #scraping ad's main information from first 'div' element
            name=job.find_all('div', class_="posting-title__wrapper")
            for n in name:
                # creting global variables and assign results of scraping to them 
                global title
                title = n.find('h4')
                global company
                company=n.find('span')              
                
            #scraping ad's further information from second 'div' element
            details =job.find_all('div', class_="posting-info position-relative d-none d-lg-flex flex-grow-1")
            for d in details:
                # creting global variables and assign results of scraping to them 
                global salary
                salary = d.find('span', class_="text-truncate badgy salary btn btn-outline-secondary btn-sm")
                global technology
                technology = d.find('object')
                global region
                region = d.find('span', class_="posting-info__location d-flex align-items-center ml-auto")
                # spliting the scrped region into a list so I can loop through its individual words in other functions
                region = region.text
                region= region.split()
                
            # spliting the scrped job ad into a list so I can loop through its individual words later in other functions
            job = job.text  
            job = job.split()

            # filtering junior permanent jobs in krk and internship anywhere
            permanent_jobs_krk_fetch(job)
            internships_anywhere_fetch(job)

        i=int(i)
        i+=1


                                              
# scraping process specific for the BulldogJobs site's structure          
def scraping_bulldog(number_of_pages):

    print ('------------------- BULLDOGJOBS -------------------', end='\n'*2)
    
    i=1
    
    # looping through indicated nuber of pages with job ads results
    while i<number_of_pages+1:
        # looping through multiple pages of results (I know there is 14 of them)
        i = str(i)
        url = 'https://bulldogjob.pl/companies/jobs/s/skills,Python?page=' + i

        # using the function to fetch all <a> elements
        jobs = jobs_fetch(url)

        #looping through all <a> elements
        for job in jobs:
            # creting global variables and assign results of scraping to them
            title = job.find('h2')
            company = job.find('div', class_='company')
            salary = job.find('div', class_='salary')
            technology = job.find('li', class_='tags-item')
            region = job.find('div', class_='location')        
            
           
            # spliting the scrped job ad into a list so I can loop through its individual words later in other functions
            job = job.text  
            job = job.split()

            
            # filtering junior permanent jobs in krk and internship anywhere
            permanent_jobs_krk_fetch(job)
            internships_anywhere_fetch(job)         
            
        i=int(i)
        i+=1
        

# using this file as a main one to call the functions (so they don't repeat in unit tests)
if __name__ == '__main__':
    no_fluffjobs(18)
    scraping_bulldog(5)
    
    
    




                      
                    
        



