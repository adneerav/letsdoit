from rest_framework import viewsets, generics, mixins, status, permissions
from rest_framework.response import Response

from movies.models import Content
from movies.serializers import ContentSerializer


class ContentAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = []  # JWT OAuth
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        print(request.user)
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


class ContentListView(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    # authentication_classes = []
    # permission_classes = []
    def list(self, request, *args, **kwargs):
        contents = Content.objects.all()
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
