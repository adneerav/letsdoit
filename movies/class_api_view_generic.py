# Create your views here.
from rest_framework import generics, mixins

from movies.models import Genre
from movies.serializers import GenreSerializer


class GenreGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                          mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    lookup_field = 'id'

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
