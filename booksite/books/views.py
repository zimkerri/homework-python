from django.http import HttpResponse
from django.shortcuts import render
from .models import Author, Genre, Book
# Create your views here.
def author_list(request):
    authors = Author.objects.all()
    authors_list = ""
    for author in authors:
        authors_list +=f"<li>{author.name}</li>"
    return HttpResponse(f"<ul>{authors_list}</ul>")

from django.http import HttpResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    text = ""

    for book in books:
        text += f"{book.title} - {book.genre.name}<br>"

    return HttpResponse(text)

from django.http import HttpResponse
from .models import Genre

def genre_list(request):
    genres = Genre.objects.all()
    text = ""

    for genre in genres:
        text += f"{genre.name}<br>"

    return HttpResponse(text)