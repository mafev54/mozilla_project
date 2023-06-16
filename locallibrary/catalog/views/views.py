from django.shortcuts import render

# Create your views here.

from ..models.author import Author
from ..models.book_instance import BookInstance
from ..models.book import Book
from ..models.genre import Genre
from ..models.languaje import Languaje

def index(request):
    """function to home site"""
    author = Author.objects.all()
    book_instance = BookInstance.objects.all()
    book = Book.objects.all()
    genre = Genre.objects.all()
    languaje = Languaje.objects.all()
    
    return render(
        request,
        'catalog/index.html',
        context = {"author":author,
                    "book_instance":book_instance,
                    "book":book,
                    "genre":genre,
                    "languaje":languaje
                    }
        )