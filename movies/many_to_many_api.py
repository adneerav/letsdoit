from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from movies.models import Genre, Content
from movies.serializers import GenreSerializer, ContentSerializer


class GenreAPIView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    @action(detail=False, methods=['POST'], name='Get content(s) by genre id')
    def get_content_by_genre(self, request):
        content_list = Content.objects.filter(genres__id__in=request.data).distinct()
        content_serializer = ContentSerializer(content_list, many=True)
        if content_list is not None and content_list.count() > 0:
            return Response(data={
                "success": True,
                "data": content_serializer.data
            }, status=status.HTTP_200_OK)
        return Response(data={
            "success": False,
            "data": {}
        }, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['POST'], name='Get Genre Detail by id')
    def get_genre_detail(self, request):
        if not request.data['id'] or not request.data['id'].isnumeric():
            return Response(data={
                'success': False,
                'message': "Invalid data type in request for id parameter.",
                'data': {}
            }, status=status.HTTP_400_BAD_REQUEST)
        genre = Genre.objects.get(pk=request.data['id'])
        genre_serializer = GenreSerializer(genre)
        return Response(data={
            'success': True,
            'message': "Data found.",
            'data': genre_serializer.data
        }, status=status.HTTP_200_OK)


class ContentAPIView(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
