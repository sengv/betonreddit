from django.test import TestCase

# Create your tests here.


from .models import Player

import random
import string
import factory



EMAIL_LIST=[
    'jwilzales55@gmail.com',
    'cbratton45@gmail.com',
    'smose913553@gmail.com',
    'creditToTeam13332@gmail.com',
    'jubileajujitsue66@gmail.com',
    'carneasantelle@gmail.com',
    'raquamarinewhale@gmail.com',
    'folylfel9999@gmail.com',
    'bob994491829904853@gmail.com'
]

def random_email():
    return EMAIL_LIST[len(EMAIL_LIST)-1]

def random_password():
    length = random.randint(8, 25)
    return u''.join(random.choice(string.ascii_letters) for x in range(length))
    

#returns a time between ~115 days ago, to now
def random_time_joined():
    return random.randint(time.time() - 10000000, now)
    
    
def random_score():
    return random.randint(1, 10000)
    
    


class UserFactory(factory.DjangoModelFactory):
      
    email = factory.LazyAttribute(lambda t: random_email())
    password = factory.LazyAttribute(lambda t: random_password())
    score = factory.LazyAttribute(lambda t: random_score())
    date_joined = factory.LazyAttribute(lambda t: random_time_joined())
    
    
class UserTestCase(TestCase):
    
    def __init__(self):
        
        self.user = UserFactory.create()
        
        
        
        
                        
    
    def test_fields_and_methods(self):
        
        assert(self.user.email in EMAIL_LIST)
        
        assert(self.user.score >= 1 and self.user.score <= 10000)
        
        self.assertTrue(isinstance(self.user, Player))
        
        new_password="mynewpassword"
        
        player.set_password(new_password)
        
        self.assertEqual(new_password, self.user.password)
        
        self.assertEqual(str(self.user), self.user.email)
        

    
    


