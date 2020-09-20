import requests
from bs4 import BeautifulSoup

            
class NoFluffJobs():

    url = "https://nofluffjobs.com/pl/jobs/python?criteria=python&page="

    def __init__ (self, job_all_details, position, company, technology, salary, region):
        #self.url = url
        self.job_all_details = job_all_details
        self.position = position
        self.company = company
        self.salary = salary
        self.technology = technology
        self.region = region

    def jobs_fetch(self,number_of_pages):

        a_list=[]
        
        i=1
        while i < number_of_pages + 1:
            i = str(i)
            url = self.url + i
                     
        #scraping results for each page
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            
        #filtering only elementswhich are <a> - like clickable job offer 
            jobs = soup.find_all('a')
            
            for job in jobs:
                a_list.append(job)
            
            i = int(i)
            i = i+1

        self.job_all_details = a_list
           
        return self.job_all_details

    def jobs_filter(self):

        key_words = ["junior", "Junior", "intern", "Intern", "Internship", "internship", "staz", "Staz", "Staż", "staż", "praktyka", "Praktyka"] 
        job_list = []
        for a in self.job_all_details:
            a = a.text
            a = a.split()
            for key_word in key_words:
                if key_word in a:
                    job_list.append(a)
            

        return print (job_list)

   
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

    
job1 = NoFluffJobs("job_all_details3", "position1", "company1", "technology1", "salary1", "region1")
job3 = NoFluffJobs("job_all_details3","position3", "company3", "technology3", "salary3", "region3")


NoFluffJobs.jobs_fetch(job3,18)
NoFluffJobs.jobs_filter(job3)




