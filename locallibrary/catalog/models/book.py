from django.db import models
from django.urls import reverse
from .author import Author
from .genre import Genre
from .languaje import Languaje


class Book(models.Model):
    title = models.CharField(max_length=200, help_text='Introduce the name of the book')
    author = models.OneToOneField(Author, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of this book')
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])