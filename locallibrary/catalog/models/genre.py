from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length = 50, help_text='Enter a book genre')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('genre-detail', args=[str(self.id)])