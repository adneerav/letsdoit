from rest_framework import viewsets, generics, mixins, status, permissions, pagination
from rest_framework.response import Response

from movies.common_response import CommonResponse
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

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class CustomPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'limit': self.page_size,
            'data': data
        })


class ContentListView(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    pagination_class = CustomPagination

    # authentication_classes = []
    # permission_classes = []
    def list(self, request, *args, **kwargs):
        contents = Content.objects.all()
        # serializer = ContentSerializer(contents, many=True, context={"request": request})
        page = self.paginate_queryset(contents)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={"request": request})
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(contents, many=True, context={"request": request})
        response_list = serializer.data
        return Response(response_list, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            formatted_response = CommonResponse. \
                get_formatted_response(success=True, message="Content data saved.",
                                       response_data=serializer.data)
            return Response(data=formatted_response, status=status.HTTP_201_CREATED)
        else:
            formatted_response = CommonResponse. \
                get_formatted_response(success=False, message=serializer.errors,
                                       response_data={})
            return Response(data=formatted_response, status=status.HTTP_400_BAD_REQUEST)
