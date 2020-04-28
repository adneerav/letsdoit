# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from movies.models import Genre
from movies.serializers import GenreSerializer


class GenreViewSet(viewsets.ViewSet):
    def list(self, request):
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # save() will call serializer's create() method
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        query_set = Genre.objects.all()
        try:
            genre = get_object_or_404(query_set, pk=pk)
        except ValueError as e:
            return Response({
                "success": False,
                "message": "Invalid data type for genre Id.",
                "exception": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        genre = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        query_set = Genre.objects.all()
        try:
            genre = get_object_or_404(query_set, pk=pk)
            genre.delete()
        except ValueError as e:
            return Response({
                "success": False,
                "message": "Invalid data type for genre Id.",
                "exception": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "success": True,
            "message": "Genre Deleted."
        }, status=status.HTTP_204_NO_CONTENT)

'''
Below view set is clone of above one.
Added to check the multiple view set in API Root
'''

class GenreSecondViewSet(viewsets.ViewSet):
    def list(self, request):
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # save() will call serializer's create() method
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        query_set = Genre.objects.all()
        try:
            genre = get_object_or_404(query_set, pk=pk)
        except ValueError as e:
            return Response({
                "success": False,
                "message": "Invalid data type for genre Id.",
                "exception": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        genre = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        query_set = Genre.objects.all()
        try:
            genre = get_object_or_404(query_set, pk=pk)
            genre.delete()
        except ValueError as e:
            return Response({
                "success": False,
                "message": "Invalid data type for genre Id.",
                "exception": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "success": True,
            "message": "Genre Deleted."
        }, status=status.HTTP_204_NO_CONTENT)