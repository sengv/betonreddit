from django.db import models
import time
# Create your models here.


class PlayerManager(models.Manager):
    
    def get_by_natural_key(self, username):
        return self.get(username=username)



class Player(models.Model):
    
    objects = PlayerManager()
    username=models.CharField(max_length=12, unique=True, default="")
        
    
    email = models.CharField(max_length=12, default="guest", unique=True)
    
    password = models.CharField(max_length=128, default="abc")
    
    score = models.PositiveIntegerField(default=100)
    
    date_joined = models.IntegerField(default=time.time)
    
    class Meta:
        unique_together=(('username'),)
    
    def __str__(self):
        
        return self.username
        
    # http://stackoverflow.com/questions/3715103/password-field-in-django-model/3715382#3715382
    #This is to prevent storing the password as plain text. I think..?
    def set_password(self, raw_password):
        import random
        algo = 'sha1'
        salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
        hsh = get_hexdigest(algo, salt, raw_password)
        self.password = '%s$%s$%s' % (algo, salt, hsh)
