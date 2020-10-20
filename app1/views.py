from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book

class Another(View):

    books = Book.objects.all()

    output = f"We have {len(books)} books"

    def get(self, request):
        return HttpResponse(self.output)

def main(equest):
    return HttpResponse('Main book view')

def reviews(request):
    return HttpResponse('Books Reviews')
