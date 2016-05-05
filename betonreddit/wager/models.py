from django.db import models
from django.core.validators import MinValueValidator

from player.models import Player
# Create your models here.



class Betline(models.Model):
    
    #Parses Reddit stream for how often <key_phrase> is used.
    key_phrase = models.TextField(default="wrong")
    
    over_under = models.IntegerField(default=1)
    
    #'over' and 'under' keeps track of when people choose over or under.
    #If lots of people choose one option, then we should adjust 'over_under' accordingly.
    over = models.IntegerField(default=0)
    under = models.IntegerField(default=0)
    
    #For bets that count total <key_phrases> in <time> in seconds. 
    time = models.IntegerField(default=1)
    
    

class Wager(models.Model):
    
    #MinValueValidator makes the minimum value be 1
    #Not sure if PositiveIntegerField is that different from IntegerField just wanted to use it once.
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    
    #When a Player is deleted, we want all of their Wagers to also be deleted.
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    
    #When a BetLine is deleted, we should still keep the data about a Wager b/c the Player still exists.
    betline = models.ForeignKey(Betline)
    
    #True = Win, False = Loss. 
    result = models.BooleanField(default=False)
    
    
    
    
    def __str__(self):
        
        
        return self.amount