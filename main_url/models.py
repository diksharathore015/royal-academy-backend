from django.db import models


    
class urls(models.Model):
    url = models.CharField(max_length=1100  ) 
    def __str__(self):
        return self.url 