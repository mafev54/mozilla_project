from django.db import models
from django.urls import reverse

class Author(models.Model):
    first_name = models.CharField(max_length=100, help_text='Introduce the name of the author')
    last_name = models.CharField(max_length=100, help_text='Introduce the last name of the author')
    date_of_birth = models.DateField(default = 0)
    date_of_death = models.DateField('Died', null=True, blank=True)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
        
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])