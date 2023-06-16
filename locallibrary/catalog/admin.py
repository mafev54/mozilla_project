from django.contrib import admin

# Register your models here.
from .models.author import Author
from .models.book_instance import BookInstance
from .models.book import Book
from .models.genre import Genre
from .models.languaje import Languaje

admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Languaje)