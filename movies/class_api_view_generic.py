# Create your views here.
from django_expiring_token.authentication import ExpiringTokenAuthentication
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from movies.models import Genre
from movies.serializers import GenreSerializer


class GenreGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                          mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    lookup_field = 'id'
    '''
    list of authentication to be applied for the api.
    BasicAuthentication will ask BasicAuthorization in api call.
    Authentication types must be assigned to authentication_classes        
    '''
    # authentication_classes = [SessionAuthentication, BasicAuthentication]

    authentication_classes = [ExpiringTokenAuthentication]
    '''
    For the token base authorization its required to add rest_framework.authtoken in
    install app settings.py.
    This is token base call
    '''

    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request, id=None):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)
