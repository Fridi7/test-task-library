from rest_framework import serializers
from .models import Writer, Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)

    class Meta:
        model = Book
        fields = ('pk', 'name')

class WriterSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    books = BookSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'books')

#req = requests.get('http://127.0.0.1:8000/api/writers/1')