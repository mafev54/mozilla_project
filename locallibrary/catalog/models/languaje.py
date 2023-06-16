from django.db import models
from django.urls import reverse
class Languaje(models.Model):
    name = models.CharField(max_length = 50, help_text='Introduce the languaje of the book')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('languaje-detail', args=[str(self.id)])