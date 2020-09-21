import requests
from bs4 import BeautifulSoup
import numpy as np

            
class NoFluffJobs():

    url = "https://nofluffjobs.com/pl/jobs/python?criteria=python&page="

    def __init__ (self, a_elements, position, company, technology, salary, region):
        #self.url = url
        self.a_elementss = a_elements
        self.position = position
        self.company = company
        self.salary = salary
        self.technology = technology
        self.region = region

    def a_element_fetch(self,number_of_pages):

        a_list=[]
        
        i=1
        while i < number_of_pages + 1:
            i = str(i)
            url = self.url + i
                     
        #scraping results for each page
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            
        #filtering only elementswhich are <a> - like clickable job offer 
            a_elements = soup.find_all('a')
            
            for a_element in a_elements:
                a_list.append(a_element)
            
            i = int(i)
            i = i+1

        self.a_elements = a_list
           
        return self.a_elements

    

   
    def jobs_details_scraping(self):

        jobs_title_and_company = []
        jobs_salary_region_tech = []

        for a_element in self.a_elements:
                
            # scraping ad's main information from first 'div' element
            name=a_element.find_all('div', class_="posting-title__wrapper")
            for n in name:
                global title
                title = n.find('h4')
             #   title= title.text
             #   self.position = title
                global company
                company=n.find('span')
              #  company = company.text
              #  self.company = company
                jobs_title_and_company.append([title, company])
                        
                    #scraping ad's more specific details from second 'div' element
            details =a_element.find_all('div', class_="posting-info position-relative d-none d-lg-flex flex-grow-1")

            for d in details:
                global salary
                salary = d.find('span', class_="text-truncate badgy salary btn btn-outline-secondary btn-sm")
               # salary =salary.text
                #self.salary = salary
                global technology
                technology = d.find('object')
                #technology = technology.text
                #self.technology = technology
                global region
                region = d.find('span', class_="posting-info__location d-flex align-items-center ml-auto")
                # spliting the scrped region into a list so I can loop through its individual words later
                #region = region.text
                #region= region.split()
                #self.region = region
                jobs_salary_region_tech.append([salary, technology, region])

        jobs_title_and_company = np.array(jobs_title_and_company, dtype=object)
        jobs_salary_region_tech = np.array(jobs_salary_region_tech, dtype=object) 

        jobs_all_details = np.concatenate((jobs_title_and_company, jobs_salary_region_tech), axis=1)
                         
        return print(jobs_all_details)




    def junior_and_intern_jobs_filter(self):

        key_words = ["junior", "Junior", "intern", "Intern", "Internship", "internship", "staz", "Staz", "Staż", "staż", "praktyka", "Praktyka"] 
        jobs_list = []
        for a_element in self.a_elements:
            a_element_copy = a_element.text
            a_element_copy = a_element_copy.split()
            for key_word in key_words:
                if key_word in a_element_copy:
                    jobs_list.append(a_element)
            
        return jobs_list

    
job1 = NoFluffJobs("job_all_details3", "position1", "company1", "technology1", "salary1", "region1")
job3 = NoFluffJobs("job_all_details3","position3", "company3", "technology3", "salary3", "region3")


NoFluffJobs.a_element_fetch(job1,18)
NoFluffJobs.jobs_details_scraping(job1)
#NoFluffJobs.junior_and_intern_jobs_filter(job3)






