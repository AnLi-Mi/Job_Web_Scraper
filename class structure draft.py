import requests
from bs4 import BeautifulSoup

class Jobs:

    def __init__ (self, url):
        self.name = name
        self.url = url
        

    def jobs_fetch(self):
    
        #scraping results for each page
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        #filtering only elementswhich are <a> - like clickable job offer 
        jobs = soup.find('a')
        return jobs
        
class NoFluffJobs(Jobs):

    def __init__ (self, job_all_details):
        self.url = "https://nofluffjobs.com/pl/jobs/python?criteria=python&page="
        self.job_all_details = jobs_fetch(self)

    def jobs_details_scraping(self):                
                
             # scraping ad's main information from first 'div' element
        name=self.job_all_details.find_all('div', class_="posting-title__wrapper")
        for n in name:
            global title
            title = n.find('h4')
            title= title.text
            global company
            company=n.find('span')
            company = company.text
                    
                #scraping ad's more specific details from second 'div' element
        details =job.find_all('div', class_="posting-info position-relative d-none d-lg-flex flex-grow-1")

        for d in details:
            global salary
            salary = d.find('span', class_="text-truncate badgy salary btn btn-outline-secondary btn-sm")
            salary =salary.text
            global technology
            technology = d.find('object')
            technology = technology.text
            global region
            region = d.find('span', class_="posting-info__location d-flex align-items-center ml-auto")
            # spliting the scrped region into a list so I can loop through its individual words later
            region = region.text
            region= region.split()
                         
        return [title, company, salary, technology, region]

    def __init__ (self, position, company, technology, salary, region):
        self.position = position
        self.company = company
        self.salary = salary
        self.technology = technology
        self.region = region



job1 = NoFluffJobs("position1", "company1", "technology1", "salary1", "region1")
job2 = NoFluffJobs(jobs_details_scraping(), "company1", "technology1", "salary1", "region1")
