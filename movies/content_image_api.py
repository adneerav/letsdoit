from django.http import Http404
from rest_framework import generics, mixins, viewsets, status
from rest_framework.exceptions import APIException
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from movies.common_response import CommonResponse
from movies.models import ContentImage, Content
from movies.serializers import ContentImageSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ContentImageAPIView(viewsets.ModelViewSet):
    serializer_class = ContentImageSerializer
    lookup_field = "id"
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        images = ContentImage.objects.all()
        return images

    def list(self, request, *args, **kwargs):
        content_id = kwargs.get("content_id")
        images = ContentImage.objects.filter(content__id=content_id)
        serializer = ContentImageSerializer(images, context={"request": request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        try:
            image_detail = ContentImage.objects.get(id=kwargs.get("id"))
        except ContentImage.DoesNotExist:
            formatted_response = CommonResponse. \
                get_formatted_response(success=False, message="Image detail not found",
                                       response_data={})
            return Response(formatted_response, status=status.HTTP_404_NOT_FOUND)
        serializer = ContentImageSerializer(image_detail, context={"request": request})
        formatted_response = CommonResponse. \
            get_formatted_response(success=False, message="Image detail found.",
                                   response_data=serializer.data)
        return Response(formatted_response, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        data = request.data
        content = Content.objects.get(id=kwargs.get("content_id"))
        image = ContentImage.objects.create(
            thumb=data["thumb"],
            type=data["type"],
            content=content
        )
        image.save()
        serializer = ContentImageSerializer(image, context={"request": request})
        success = True if serializer.is_valid(raise_exception=True) else False
        message = "Image saved successfully." if success else serializer.errors
        formatted_response = CommonResponse. \
            get_formatted_response(success=success, message=message, response_data=serializer.data)
        return Response(formatted_response, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        try:
            content_image = ContentImage.objects.get(id=kwargs.get("id"))
            content_image.delete()
            formatted_response = CommonResponse. \
                get_formatted_response(success=True, message="Image deleted successfully",
                                       response_data={})
            return Response(formatted_response, status=status.HTTP_204_NO_CONTENT)
        except ContentImage.DoesNotExist:
            formatted_response = CommonResponse. \
                get_formatted_response(success=False, message="Image not found.",
                                       response_data={})
            return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            queryset = ContentImage.objects.get(id=kwargs.get("id"))
        except ContentImage.DoesNotExist:
            formatted_response = CommonResponse. \
                get_formatted_response(success=False, message="Image not found.",
                                       response_data={})
            return Response(data=formatted_response, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        content = Content.objects.get(image__id=kwargs.get("id"))
        if content is None or content.id is None:
            formatted_response = CommonResponse. \
                get_formatted_response(success=True, message="Content not found for this Image.",
                                       response_data={})
            return Response(formatted_response, status=status.HTTP_404_NOT_FOUND)
        queryset.thumb = data["thumb"]
        queryset.type = data["type"]
        queryset.content = content
        queryset.save()
        serializer = ContentImageSerializer(queryset, context={"request": request})
        formatted_response = CommonResponse. \
            get_formatted_response(success=True, message="Image updated successfully.",
                                   response_data=serializer.data)
        return Response(data=formatted_response)
