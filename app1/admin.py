from django.contrib import admin
from .models import Book, BookNumber, Character

# Register your models here.

admin.site.register(Book)
admin.site.register(BookNumber)
admin.site.register(Character)
