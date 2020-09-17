import unittest
# from job_web_scraper import jobs_fetch
from Job_Web_Scraper import job_web_scraper

class Job_Web_Scraper_testing(unittest.TestCase):

    def test_a_element_scraping(self):
        url = "https://www.onet.pl/"
        x = job_web_scraper.jobs_fetch(url)[0].text.split()
        x = "".join(x)
        self.assertEqual(x, "Onet")


if __name__ == '__main__':
    unittest.main()



    
 
