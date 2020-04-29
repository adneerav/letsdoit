from rest_framework import viewsets

from movies.models import Genre, Content
from movies.serializers import GenreSerializer, ContentSerializer


class GenreAPIView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ContentAPIView(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
