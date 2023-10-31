from django.shortcuts import render
from .models import Book


# Create your views here.

def index(request):
  books = Book.objects.all()
  return render(request, "book_outlet/index.html", {
    "books": books
  })

def book_detail(request, id):
  book = Book.objects.get(pk=id) # pk stands for primary key defined in our database. 
  return render(request, "book_outlet/index.html", {
    "title": book.title,
    "author": book.author,
    "rating": book.rating,
    "is_bestseller": book.is_bestseller
  })
  