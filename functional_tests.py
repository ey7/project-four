"""
code credit: https://www.obeythetestinggoat.com/book/chapter_02.html
"""
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_access_the_online_shop(self):  
        # This is a test to see if the shop is working on localhost
       
        self.browser.get('http://localhost:8000')

        # test whether online shop is in the title
        self.assertIn('Racquets', self.browser.title)  
          
if __name__ == '__main__':  
    unittest.main()  