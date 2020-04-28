# Create your views here.
from django.http import HttpResponse
from rest_framework import status, generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import Genre
from movies.serializers import GenreSerializer


class GenreGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                          mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    lookup_field = 'id'
    '''
    list of authentication to be applied for the api.
    BasicAuthentication will ask BasicAutorization in api call.
    Authentication types must be assigned to authentication_classes        
    '''
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)
