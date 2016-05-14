from selenium import webdriver

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils.translation import activate
from django.core.urlresolvers import reverse

from django.test import Client


class TestBeginning(StaticLiveServerTestCase):
    
    
    def setUp(self):
        
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
        self.client = Client()        
        activate('en')
        
        
        
    def tearDown(self):
        self.browser.quit()
        
        
    
    def test_homepage_title(self):
        
        #self.browser.get(self.get_full_url("home"))
        self.browser.get("http://localhost:8081")
        
        assert ("Bet on Reddit" in self.browser.title)
        
        
        
    def test_status_codes(self):
        
        #status 200 means all is well.
        home_page = self.client.post('', {})
        self.assertEqual(home_page.status_code, 200)
        
        
        #status 301 is "permanently redirected" to page not found.
        subreddit_view = self.client.post('/subreddit/a', {})
        self.assertEqual(subreddit_view.status_code, 301)
        
        
        
        
    def test_url_reverses(self):
        
        
        #reverse() takes in whatever name the url was given. 
        #it returns the url. 
        home_reversed = reverse("home")
        self.assertEqual(home_reversed, '/')

        subreddit_reversed = reverse("subreddit", args=["pics"])
        self.assertEqual(subreddit_reversed, "/subreddit/pics/")
        
        
        
    
        
        
        
        
    
    

