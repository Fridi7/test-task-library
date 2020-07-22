from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Writer, Book
from .serializers import BookSerializer, WriterSerializer
from django.http import Http404
from rest_framework.generics import get_object_or_404


class WriterView(APIView):

    # def get(self, request):
    #     books = Book.objects.all()
    #     #return Response({"articles": articles})
    #
    #     serializer = BookSerializer(books, many=True)
    #     return Response({"books": serializer.data})

    def get(self, request, pk):
        try:
            writer_id = Writer.objects.get(pk=pk)
            serializer = WriterSerializer(writer_id)
        except Book.DoesNotExist:
            raise Http404()

        return Response(serializer.data)


class BookView(APIView):

    # def get(self, request):
    #     books = Book.objects.all()
    #     #return Response({"articles": articles})
    #
    #     serializer = BookSerializer(books, many=True)
    #     return Response({"books": serializer.data})

    def get(self, request, pk):
        try:
            book_id = Book.objects.get(pk=pk)
            serializer = BookSerializer(book_id)
        except Book.DoesNotExist:
            raise Http404()

        return Response({"book": serializer.data})
