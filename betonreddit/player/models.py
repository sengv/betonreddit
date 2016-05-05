from django.db import models
import time
# Create your models here.



class Player(models.Model):
    
    
    username = models.CharField(max_length=12, default="guest")
    
    score = models.PositiveIntegerField(default=100)
    
    date_joined = models.IntegerField(default=time.time)
    
    
    def __str__(self):
        
        return self.username