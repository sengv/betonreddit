from django.db import models
from django.core.validators import MinValueValidator

from player.models import Player
# Create your models here.



class Betline(models.Model):
    
    
    
    #Parses Reddit stream for how often <key_phrase> is used.
    key_phrase = models.TextField(default="hello")
    
    amount = models.IntegerField(default=1)
    
    #For bets that count total <key_phrases> in <time> in seconds. 
    duration = models.IntegerField(default=1)
    
    
    class Meta:
        unique_together=["key_phrase", "amount", "duration"]
    
    
    def __str__(self):
        
        
        return key_phrase
    
    

class Wager(models.Model):
    

    amount = models.IntegerField(default=1)
    
    #When a Player is deleted, we want all of their Wagers to also be deleted.
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    
    #When a BetLine is deleted, we should still keep the data about a Wager b/c the Player still exists.
    betline = models.ForeignKey(Betline)
    
    options = (("over", "over"),
               ("under", "under"),        
    )
    
    over_OR_under = models.CharField(max_length=8, choices=options, default="")
    
    #True = Win, False = Loss. 
    result = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ["amount", "player", "betline", "over_OR_under"]

    def __str__(self):
        
        return str(player.id) + "/" + str(betline)