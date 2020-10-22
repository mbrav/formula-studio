from rest_framework import serializers
from .models import Book, BookNumber, Character, Author

class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['id', 'sibn_10', 'sibn_13']

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'surname']

class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many = False)
    characters = CharacterSerializer(many = True)
    authors = AuthorSerializer(many = True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'number', 'characters', 'authors']
