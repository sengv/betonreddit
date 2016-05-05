from urllib.request import Request, urlopen
import json

REDDIT_URL = "https://www.reddit.com"
SUB_TEMPLATE = REDDIT_URL + "/r/{subreddit}.json"

class subreddit(object):
    def __init__(self, sub_name):
        self.name = sub_name
        self.raw  = None
        self.json = {}

        self.posts = None
    
    def __str__(self):
        return '/r/%s' % self.name
    
    def loadData(self):
        req = Request(SUB_TEMPLATE.replace('{subreddit}',
                                           self.name))
        
        # Need user agent otherwise Reddit rejects the request
        req.add_header('User-Agent', 'betonreddit')
        raw = urlopen(req)
        
        # Decodes to a string so JSON object can parse it
        rawData = raw.read().decode("utf-8")
        jsonData = json.loads(rawData)
        
        self.raw = rawData
        self.json = jsonData

        jsonData = jsonData.get('data')
        # jsonData will be none if there is an error, hopefully this stops
        # exceptions from occuring
        if jsonData:
            # Posts are stored in the children object
            self.posts = jsonData['children']
        
    def get(self, elem):
        return self.__dict__.get(elem)
