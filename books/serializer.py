from rest_framework import serializers
from .models import Book, BookImage


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = BookImage
        fields = ['books', 'image']

class BookSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many = True, read_only = True)
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'isbn', 'descriptions', 'total_copies', 'available_copies', 
                    'published_date', 'created_at', 'images']