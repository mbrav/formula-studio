from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book

class Another(View):

    books = Book.objects.all()

    output = ''

    for book in books:
        output += f"We have {book.title} book in DB with ID {book.id} <br>"

    def get(self, request):
        return HttpResponse(self.output)

def main(equest):
    return HttpResponse('Main book view')

def reviews(request):
    return HttpResponse('Books Reviews')
