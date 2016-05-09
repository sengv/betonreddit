from selenium import webdriver

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils.translation import activate



class TestBeginning(StaticLiveServerTestCase):
    
    
    def setUp(self):
        
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)
        
        activate('en')
        
        
    def tearDown(self):
        self.browser.quit()
        
        
    
    def test_homepage_title(self):
        
        #self.browser.get(self.get_full_url("home"))
        self.browser.get("http://localhost:8081")
        
        assert "Bet on Reddit" in self.browser.title
        
        
    
    

