from django.http import HttpResponse
from django.shortcuts import render

from .models import Book


def index(request):
    books = Book.objects.all()
    context = {'books': books, 'title': 'Список книг'}
    return render(request, template_name='lib/index.html', context=context)


def test(request):
    return HttpResponse('<h1>Test Page</h1>')