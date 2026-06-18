from django.contrib import admin
from django.urls import path, include
from .views import author_list
from .views import author_list, genre_list, book_list
urlpatterns = [
    path('authors-list/', author_list),
    path('genres/', genre_list),
    path('books/', book_list),
]
