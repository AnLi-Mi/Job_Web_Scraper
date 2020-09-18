import unittest
# from job_web_scraper import jobs_fetch
from Job_Web_Scraper import job_web_scraper

class Job_Web_Scraper_testing(unittest.TestCase):

    def test_a_element_scraping(self):
        url = "https://www.onet.pl/"
        x = job_web_scraper.jobs_fetch(url)[0].text.split()
        x = "".join(x)
        self.assertEqual(x, "Onet")

    def test_internship_keywords(self):
        jobs = job_web_scraper.jobs_fetch("https://nofluffjobs.com/pl/jobs?criteria=oracle&page=3")
        a = []
        b=[]
        for job in jobs:
            job = job.text  
            job = job.split()
            try:
                result = job_web_scraper.internships_anywhere_fetch(job)
                print (result)
                a.append(result)
            except NameError:
                pass
        print(a)
            
        for result in a:
            if result != None:
                b.append(result)
                
        results = b[0]
                
        self.assertEqual (results, "Oracle ADF Developer Intern w COMP S.A. miccheck_circle 12 800 - 19 200 PLN java Warszawa, POL")
    


if __name__ == '__main__':
    unittest.main()



    
 
