from django.db import models

class Author(models.Model):
    name = models.CharField(max_length = 50)
    date_of_birth = models.DateTimeField(auto_now = True)
    date_of_death = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name 
        