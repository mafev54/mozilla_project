from django.urls import path

from .views import views
from .views import author
from .views import book_instance
from .views import book
from .views import genre
from .views import languaje

urlpatterns = [
    
    path('', views.index, name= "index")
]

urlpatterns += [
    path("author/", author.AuthorListView.as_view(),name="authors"),
    path("author/<int:pk>",author.AuthorDetailView.as_view(),name='author-detail'),
    path("author/create", author.AuthorCreateView.as_view(),name='create-author')
]

urlpatterns += [
    path("book_instance/", book_instance.BookInstanceListView.as_view(),name="book_instances"),
    path("book_instance/<int:pk>",book_instance.BookInstanceDetailView.as_view(),name='book_instance-detail'),
    path("book_instance/create", book_instance.BookInstanceCreateView.as_view(),name='create-book_instance')
]

urlpatterns += [
    path("book/", book.BookListView.as_view(),name="books"),
    path("book/<int:pk>",book.BookDetailView.as_view(),name='book-detail'),
    path("book/create", book.BookCreateView.as_view(),name='create-book')
]

urlpatterns += [
    path("genre/", genre.GenreListView.as_view(),name="genres"),
    path("genre/<int:pk>",genre.GenreDetailView.as_view(),name='genre-detail'),
    path("genre/create", genre.GenreCreateView.as_view(),name='create-genre')
]

urlpatterns += [
    path("languaje/", languaje.LanguajeListView.as_view(),name="languajes"),
    path("languaje/<int:pk>",languaje.LanguajeDetailView.as_view(),name='languaje-detail'),
    path("languaje/create", languaje.LanguajeCreateView.as_view(),name='create-languaje')
]
