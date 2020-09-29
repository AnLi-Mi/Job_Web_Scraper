#STEPS OF THE PROGRAM:
#
#1. scraping each site of website results to find <a> elements as job ads are presented
# in a clickable <a> elements and placing them into a list 'a_list' in their HTML format
# - method of JobSites class, the same for all websites
#
#2. looping through all <a> elements in the list to fatch specific information
# about each job: title, company, salary, technology, region and placing them
# in a new list 'jobs_all_details' (still in HTML format) - method spacific for each website/
# each child class as each site has different structure
#
#3. connecting 'jobs_all_details' lists from different child classes and looping
# through their elements to find key words descripitng the job titles or
# job location to filter the required ones and put them to a new list 'my_jobs_list" -
# the same method for all websites - method of parent class
#
#4. looping through all elements of 'my_jobs_list', modify them to a text/string
# format and present them nicely
#
#5. turning all filtred jobs into an object of Jobs class and assing their details
# as class attribute
#
#6. calling all the methods to dispaly all the results






import requests
from bs4 import BeautifulSoup


# creating a class for all filtered jobs scrapped from the job sites
class Jobs:
    def __init__ (self, name, position, company, technology, salary, region):
        self.name = name
        self.position = position
        self.company = company
        self.salary = salary
        self.technology = technology
        self.region = region

    def __str__(self):     
        return f"{self.name}\n Title: {self.position},\n Company: {self.company},\n Salary: {self.salary},\n Technology: {self.technology},\n Region: {self.region}\n\n\n"

# creating a class for websites with job offer we want to scrape    
class JobSites:
    def __init__ (self, name):
        self.name = name
        
        
    #fetching all <a> elements as job ads are presented as <a> elements
    def a_element_fetch(self,number_of_pages):

        a_list=[]
        i=1

        #looping through the given nuber of pages with results
        while i < number_of_pages + 1:
            i = str(i)
            url = self.url + i
                     
            #scraping results for each page
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            
            #filtering only elements which are <a> - like clickable job offer 
            a_elements = soup.find_all('a')

            #looping through fetched <a> elements to add each to the list of <a> elements
            for a_element in a_elements:
                a_list.append(a_element)
            
            i = int(i)
            i = i+1
 
        return a_list

     # function filtering only jobs' ads with key word "internship" in it
    def intern_jobs_filter(self, number_of_pages):

        key_words = ["intern", "Intern", "Internship", "internship", "staz", "Staz", "Staż", "staż", "praktyka", "Praktyka"] 
        my_internships_list = []
        jobs_all_details = []
       
        jobs_all_details_NF = NoFluffJobs.jobs_details_scraping(self, number_of_pages)
       # jobs_all_details_NF = np.array(jobs_all_details_NF, dtype=object)
        jobs_all_details_BD = BulldogJobs.jobs_details_scraping(self, number_of_pages)
       # jobs_all_details_BD = np.array(jobs_all_details_BD, dtype=object)
       # jobs_all_details = np.vstack((jobs_all_details_BD, jobs_all_details_NF))

        for job in jobs_all_details_NF:
           jobs_all_details.append(job)

        for job in jobs_all_details_BD:
           jobs_all_details.append(job)


        print (f'Internships jobs to filter: {len(jobs_all_details)}')

                
        for job in jobs_all_details:
                        
            job_title = job[0]
            job_title = job_title.text
            job_title = job_title.split()
            for key_word in key_words:
                if key_word in job_title:
                    my_internships_list.append(job)
                    
        print (f'Internships result: {len(my_internships_list)}')
                       
        return my_internships_list

    # function filtering only jobs's ads with key word "Junior" in it and location in Kraków
    def KRKjunior_jobs_filter(self, number_of_pages):

        permanent_key_words = ["Junior"]
        locations = ["Warszawa", "Warszawa,", "Kraków,", "kraków,", "cracow,", "Cracow,", "Krakow,", "krakow,", "zdalna,", "Zdalna,", "zdalna", "Zdalna"]
        my_junior_list = []
        jobs_all_details = []
       
        jobs_all_details_NF = NoFluffJobs.jobs_details_scraping(self, number_of_pages)
       # jobs_all_details_NF = np.array(jobs_all_details_NF, dtype=object)
        jobs_all_details_BD = BulldogJobs.jobs_details_scraping(self, number_of_pages)
       # jobs_all_details_BD = np.array(jobs_all_details_BD, dtype=object)
       # jobs_all_details = np.vstack((jobs_all_details_BD, jobs_all_details_NF))

        for job in jobs_all_details_NF:
           jobs_all_details.append(job)

        for job in jobs_all_details_BD:
           jobs_all_details.append(job)

        print (f'KRKjunior jobs to filter: {len(jobs_all_details)}')

                 
        for job in jobs_all_details:
                
            job_title = job[0]
            job_title = job_title.text
            job_title = job_title.split()
            
            for key_word in permanent_key_words:
                print (key_word)
                if key_word in job_title:
                    print (key_word)
                    print (job_title)
                    print('-------------------')
                    for location in locations:
                        #print (location)
                        region = job[4]
                        region = region.text
                        region = region.split()
                        if location in region:
                            #print ('-------------------------')
                            #print(f'Job: {job_title}')
                            #print(f'Region: {region}')
                            #print(f'Key word lokation: {location}')
                            #print ('-------------------------')
                            my_junior_list.append(job)

        print (f'KRKjunior jobs results: {len(my_junior_list)}')
                        
        return my_junior_list

        
    # method creating Jobs class object from filtered jobs ads
    def job_objects_generator(self, number_of_pages):
                
        global job_objects_list
        job_objects_list = []

        i = 1

        my_internships_list= JobSites.intern_jobs_filter(self, number_of_pages)
        my_junior_list = JobSites.KRKjunior_jobs_filter(self, number_of_pages)

        my_jobs_list = my_internships_list + my_junior_list

        # displaying the job details neatly
        for job in my_jobs_list:
            global title
            title = job[0]
            i = str(i)
            global name
            name = "Job "+i
            i = int(i)
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


            # creating job objects
            global x

            x = Jobs(name, title, company, technology, salary, region)
            job_objects_list.append(x)

            i=i+1
            
    #trying to assing the created objects to unique variables
    def assign_variable_to_object(self):

        import gc
        lista = []

        k=1
        for obj in gc.get_objects():
            if isinstance(obj, Jobs):
                exec(f'global job_{k}')
                exec(f'job_{k} = obj')
                print (job_1.name, job_1.salary)
                exec(f'print(job_{k}.name)')
                k+=1
    
# creating a child class for the all sites with results in NoFluffJobs            
class NoFluffJobs(JobSites):
    # creating a class attribute 
    url = "https://nofluffjobs.com/pl/jobs/python?criteria=python&page="   
  
    # fatching specific information about the job from each <a> element's content
    def jobs_details_scraping(self, number_of_pages):

        # jobs_title_and_company = []
        # jobs_salary_region_tech = []

        # calling a method of JobSites class
        a_elements = JobSites.a_element_fetch(self, number_of_pages)
        jobs_all_details = []

        for a_element in a_elements:

            job_all_details=[]
                
            # scraping ad's main information from first 'div' element and adding them to a list
            name=a_element.find_all('div', class_="posting-title__wrapper")
            for n in name:
                global title
                title = n.find('h4')
                global company
                company=n.find('span')
                job_all_details.append(title)
                job_all_details.append(company)
                
                        
            #scraping ad's further information details from second 'div' element and adding them to a list
            details =a_element.find_all('div', class_="posting-info position-relative d-none d-lg-flex flex-grow-1")

            for d in details:
                global salary
                salary = d.find('span', class_="text-truncate badgy salary btn btn-outline-secondary btn-sm")               
                global technology
                technology = d.find('object')                
                global region
                region = d.find('span', class_="posting-info__location d-flex align-items-center ml-auto")
                job_all_details.append(salary)
                job_all_details.append(technology)
                job_all_details.append(region)
                # spliting the scrped region into a list so I can loop through its individual words later

                   
            if job_all_details:
                jobs_all_details.append(job_all_details)                     
                                  
        return (jobs_all_details)

    

class BulldogJobs(JobSites):

    url = "https://bulldogjob.pl/companies/jobs/s/skills,Python?page="

    def jobs_details_scraping(self, number_of_pages):

        jobs_all_details = []
        # calling a method of JobSites class
        a_elements = JobSites.a_element_fetch(self, number_of_pages)
       
        #looping through all <a> elements
        for a_element in a_elements:
            # creting global variables and assign results of scraping to them
            global title
            title = a_element.find('h4', class_="posting-title__position")
            global company
            company = a_element.find('span', class_="posting-title__company")
            global salary
            salary = a_element.find('span', class_='text-truncate badgy salary btn btn-outline-secondary btn-sm')
            global technology
            technology = a_element.find('a', class_="btn text-truncate btn-outline-secondary btn-sm")
            global region
            region = a_element.find('span', class_='posting-info__location d-flex align-items-center ml-auto')

            if title is not None:
                jobs_all_details.append([title, company, salary, technology, region])

        
        return (jobs_all_details)




   


     

# creating an object of NoFluffJobs class            
job_site1= NoFluffJobs("nofluff")
job_site2= BulldogJobs("bulldog")



NoFluffJobs.job_objects_generator(job_site1,18)
BulldogJobs.job_objects_generator(job_site2,18)

#NoFluffJobs.assign_variable_to_object(job_site1)









