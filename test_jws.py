import unittest
from job_web_scraper import jobs_fetch


class Job_Web_Scraper_testing(unittest.TestCase):

    def test_a_element_scraping(self):
        url = "https://www.onet.pl/"
        x = jobs_fetch(url)
        #x = x[0].text
        self.assertEqual(x.text, "Onet")
        
    
