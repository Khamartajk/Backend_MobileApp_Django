from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer 


@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serialized_data = BookSerializer(books, many=True)
    if not books:
        return Response({"message": "No books found"}, status=status.HTTP_404_NOT_FOUND)
    return Response(serialized_data.data, status=status.HTTP_200_OK)
    

@api_view(['POST']) 
def add_book(request):
   data = request.data
   serialized_data = BookSerializer(data=data)
   if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
   return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    data = request.data
    serialized_data = BookSerializer(book, data=data)
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
