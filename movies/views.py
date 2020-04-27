from django.http import Http404, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser

from movies.models import Genre
from movies.serializers import GenreSerializer

''' 
This is using without any generic api view.
Only simple serializers & json parser default classes.
without csrf_exept annotation it wont allow to request from postman.
https://docs.djangoproject.com/en/3.0/ref/csrf/#django.views.decorators.csrf.csrf_exempt
'''


@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        '''
        What is many = True ?
        To serialize a queryset or list of objects instead of a single
        object instance, you should pass the many=True flag when 
        instantiating the serializer. You can then pass a queryset 
        or list of objects to be serialized.
        '''

        '''
        What is safe ?
        By default JsonResponse first param(serializer.data) should be 
        dict.But here its list so safe = False will allow to convert in
        list. 
        https://docs.djangoproject.com/en/3.0/ref/request-response/#jsonresponse-objects
        '''
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = GenreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # save() will call serializer's create() method
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
