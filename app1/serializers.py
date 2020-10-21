from rest_framework import serializers
from .models import Book
from .models import BookNumber

class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['id', 'sibn_10', 'sibn_13']

class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many = False)
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'price', 'number']
