from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book

# def main(request):
#     return render(request, 'book-main.html', {
#         'data': {
#             'books': Book.objects.all()
#         }
#     })
#
# class Another(View):
#
#     books = Book.objects.all()
#
#     output = ''
#
#     for book in books:
#         output += f"We have {book.title} book in DB with ID {book.id} <br>"
#
#     def get(self, request):
#         return HttpResponse(self.output)

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
