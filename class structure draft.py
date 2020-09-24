import requests
from bs4 import BeautifulSoup
import numpy as np


class Jobs:
    def __init__ (self, position, company, technology, salary, region):
        self.position = position
        self.company = company
        self.salary = salary
        self.technology = technology
        self.region = region

    def __str__(self):
     
        return f" Title: {self.position},\n Company: {self.company},\n Salary: {self.salary},\n Technology: {self.technology},\n Region: {self.region}\n\n\n"
    
class JobSites():

    def __init__ (self, url):
        self.url=url

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

                
        return a_list

    
            
class NoFluffJobs(JobSites):

    url = "https://nofluffjobs.com/pl/jobs/python?criteria=python&page="

    def __init__ (self):
        pass
    
  
   
    def jobs_details_scraping(self, number_of_pages):

        jobs_title_and_company = []
        jobs_salary_region_tech = []
        a_elements = JobSites.a_element_fetch(self, number_of_pages)

        for a_element in a_elements:
                
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

       
                         
        return (jobs_all_details)




    def intern_jobs_filter(self, number_of_pages):

        key_words = ["intern", "Intern", "Internship", "internship", "staz", "Staz", "Staż", "staż", "praktyka", "Praktyka"] 
        my_internships_list = []
        jobs_all_details = NoFluffJobs.jobs_details_scraping(self, number_of_pages)
        for job in jobs_all_details:            
            
            job_title = job[0]
            job_title = job_title.text
            job_title = job_title.split()
            for key_word in key_words:
                if key_word in job_title:
                    my_internships_list.append(job)

                       
        return my_internships_list

    def KRKjunior_jobs_filter(self, number_of_pages):

        permanent_key_words = ["junior", "Junior"]
        locations = ["Kraków,", "kraków,", "cracow,", "Cracow,", "Krakow,", "krakow,", "zdalna,", "Zdalna,", "zdalna", "Zdalna"]
        my_junior_list = []

        jobs_all_details = NoFluffJobs.jobs_details_scraping(self, number_of_pages)
        for job in jobs_all_details:            
    
            job_title = job[0]
            job_title = job_title.text
            job_title = job_title.split()
            
            for key_word in permanent_key_words:
                if key_word in job_title:
                    for location in locations:
                        region = job[4]
                        region = region.text
                        region = region.split()
                        if location in region:
                            my_junior_list.append(job)

            self.my_junior_list = my_junior_list
            
        return self.my_junior_list

        

    def job_objects_generator(self, number_of_pages):

        print ("JOB OFFERS FROM NOFLUFFJOBS SITE:")
          
        job_objects_list = []

        i = 1

        my_internships_list= NoFluffJobs.intern_jobs_filter(self, number_of_pages)
        my_junior_list = NoFluffJobs.KRKjunior_jobs_filter(self, number_of_pages)

        my_jobs_list = my_internships_list + my_junior_list
        
        for job in my_jobs_list:
            global title
            title = job[0]
            try:
                title = title.text.strip()
            except AttributeError:
                title = "No Info"
                
            global company
            company = job[1]
            try:
                company= company.text.strip()
            except AttributeError:
                company = "No Info"

            global salary    
            salary = job[2]
            try:
                salary= salary.text.strip()
            except AttributeError:
                salary = "No Info"

            global technology    
            technology = job[3]
            try:
                technology = technology.text.strip()
            except AttributeError:
                technology = "No Info"

            global region    
            region = job[4]
            try:
                region = region.text.strip()
            except AttributeError:
                region = "No Info"

                               

            print (f" JOB no {i}:\n Title: {title},\n Company: {company},\n Salary: {salary},\n Technology: {technology},\n Region: {region}\n\n\n")

            x = Jobs(title, company, technology, salary, region)
            job_objects_list.append(x)

            i=i+1

        global job1
        job1=job_objects_list[0]
        global job2
        job2=job_objects_list[1]
        global job3
        job3=job_objects_list[2]
        global job4
        job4=job_objects_list[3]
        global job5
        job5=job_objects_list[4]
        global job6
        job6=job_objects_list[5]
        global job7
        job7=job_objects_list[6]
        global job8
        job8=job_objects_list[7]
        global job9
        job9=job_objects_list[8]
        global job10
        job10=job_objects_list[9]
        global job11
        job11=job_objects_list[10]
        global job12
        job12=job_objects_list[11]
        global job13
        job13=job_objects_list[12]

                
        return job_objects_list, job1, job2, job3, job4, job5, job6, job7, job8, job9, job10, job11, job12, job13

           
job_site1= NoFluffJobs()


#NoFluffJobs.jobs_details_scraping(job_site1,18)
#NoFluffJobs.intern_jobs_filter(job_site1)
#NoFluffJobs.KRKjunior_jobs_filter(job_site1)
NoFluffJobs.job_objects_generator(job_site1,18)









