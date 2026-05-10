from rest_framework import serializers
from .models import Book, BookImage

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = BookImage
        fields = '__all__'