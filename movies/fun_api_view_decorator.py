# Create your views here.
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movies.models import Genre
from movies.serializers import GenreSerializer

'''
function based decorator api_view have receive instance of Request
& return as a Response.

if api_view() does not have any specified method , it will take GET as 
default & for the rest request it will give 405 error
'''


@api_view(['GET', 'POST'])
def genre_list(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # save() will call serializer's create() method
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def genre_detail(request, pk):
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        '''
        What is DoesNotExist ?
        This exception is raised by the ORM in a couple places,
        for example by QuerySet.get() when an object is not found
        for the given query parameters.
        https://docs.djangoproject.com/en/3.0/ref/models/instances/#django.db.models.Model.DoesNotExist
        '''
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = GenreSerializer(genre)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        genre = genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
