from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)


class WriterSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    books = BookSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'books')
