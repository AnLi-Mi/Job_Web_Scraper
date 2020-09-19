import requests
from bs4 import BeautifulSoup

            
class NoFluffJobs():

    def __init__ (self, url, job_all_details, position, company, technology, salary, region):
        self.url = url
        self.job_all_details = job_all_details
        self.position = position
        self.company = company
        self.salary = salary
        self.technology = technology
        self.region = region

    def jobs_fetch(self,number_of_pages):

        jobs_list=[]
        
        i=1
        while 1< number_of_pages + 1:
            i = str(i)
            url = self.url + i  
    
        #scraping results for each page
        
            page = requests.get(self.url)
            soup = BeautifulSoup(page.content, 'html.parser')
        #filtering only elementswhich are <a> - like clickable job offer 
            job = soup.find_all('a', class_="posting-list-item posting-list-item--businessIntelligence highlightId-ZGZ7TSHK")
            jobs_list.append(job)
            i = int(i)
            i = i+1    
            
            
        return print(jobs_list)

    def jobs_details_scraping(self):                
                
             # scraping ad's main information from first 'div' element
        name=self.job_all_details.find_all('div', class_="posting-title__wrapper")
        for n in name:
            global title
            title = n.find('h4')
            title= title.text
            self.position = title
            global company
            company=n.find('span')
            company = company.text
            self.company = company
                    
                #scraping ad's more specific details from second 'div' element
        details =self.job_all_details.find_all('div', class_="posting-info position-relative d-none d-lg-flex flex-grow-1")

        for d in details:
            global salary
            salary = d.find('span', class_="text-truncate badgy salary btn btn-outline-secondary btn-sm")
            salary =salary.text
            self.salary = salary
            #global technology
            #technology = d.find('object')
            #technology = technology.text
            #self.technology = technology
            global region
            region = d.find('span', class_="posting-info__location d-flex align-items-center ml-auto")
            # spliting the scrped region into a list so I can loop through its individual words later
            region = region.text
            region= region.split()
            self.region = region
                         
        return self.position, self.company, self.salary, self.technology, self.region

    
job1 = NoFluffJobs("https://nofluffjobs.com/pl/jobs/python?criteria=python&page","job_all_details3", "position1", "company1", "technology1", "salary1", "region1")
job3 = NoFluffJobs("https://nofluffjobs.com/pl/jobs/python?criteria=python&page","job_all_details3","position3", "company3", "technology3", "salary3", "region3")


NoFluffJobs.jobs_fetch(job3,3)
NoFluffJobs.jobs_details_scraping(job3)



