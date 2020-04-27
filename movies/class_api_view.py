# Create your views here.
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import Genre
from movies.serializers import GenreSerializer


class GenreAPIView(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # save() will call serializer's create() method
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Genre.objects.get(id=id)
        except Genre.DoesNotExist:
            '''
            What is DoesNotExist ?
            This exception is raised by the ORM in a couple places,
            for example by QuerySet.get() when an object is not found
            for the given query parameters.
            https://docs.djangoproject.com/en/3.0/ref/models/instances/#django.db.models.Model.DoesNotExist
            '''
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        genre = self.get_object(id)
        if isinstance(genre, Response) and genre.status_code == status.HTTP_404_NOT_FOUND:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request, id):
        genre = self.get_object(id)
        if isinstance(genre, Response) and genre.status_code == status.HTTP_404_NOT_FOUND:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        genre = self.get_object(id)
        if isinstance(genre, Response) and genre.status_code == status.HTTP_404_NOT_FOUND:
            return Response(status=status.HTTP_404_NOT_FOUND)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
