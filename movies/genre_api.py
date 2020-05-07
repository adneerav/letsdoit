from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.common_response import CommonResponse
from movies.models import Genre
from movies.serializers import GenreSerializer


def is_genre_exist(name):
    genre = Genre.objects.filter(name=name)
    return genre.count() > 0


def get_object(id=None):
    try:
        return Genre.objects.get(id=id)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


class GenreAPI(APIView):
    def get(self, request):
        qs_genre = Genre.objects.all()
        genre_serializer = GenreSerializer(qs_genre, many=True)
        success = True if qs_genre.count() > 0 else False
        message = "Genre(s) list found." if success else "No Genre(s) data found."
        formatted_response = CommonResponse.get_formatted_response(
            success=success, response_data=genre_serializer.data, message=message)
        return Response(formatted_response, status=status.HTTP_200_OK)

    def post(self, request):
        genre_serializer = GenreSerializer(data=request.data)
        if genre_serializer.is_valid():
            if is_genre_exist(name=request.data["name"]):
                '''
                Check if genre already exist.
                Response accordingly
                '''
                formatted_response = CommonResponse.get_formatted_response(
                    success=False, response_data=genre_serializer.data,
                    message="Genre name already exist.")
                return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)
            '''
            No duplicate genre. save the data
            & response accordingly
            '''
            genre_serializer.save()
            formatted_response = CommonResponse.get_formatted_response(
                success=True, response_data=genre_serializer.data,
                message="Genre saved successfully.")
            return Response(formatted_response, status=status.HTTP_201_CREATED)
        '''
        Default response & message for the bad request.
        '''
        formatted_response = CommonResponse.get_formatted_response(
            success=False, response_data=genre_serializer.data,
            message=genre_serializer.errors)
        return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)


class GenreDetail(APIView):
    def get(self, request, id=None):
        genre = get_object(id)
        if isinstance(genre, Response) and genre.status_code == status.HTTP_404_NOT_FOUND:
            formatted_response = CommonResponse.get_formatted_response(
                message="Genre details not found.", success=False, response_data={}
            )
            return Response(data=formatted_response, status=status.HTTP_404_NOT_FOUND)
        serializer_genre = GenreSerializer(genre)
        formatted_response = CommonResponse.get_formatted_response(
            message="Genre details found.", success=True,
            response_data=serializer_genre.data)
        return Response(formatted_response, status=status.HTTP_200_OK)

    def put(self, request, id=None):
        genre = get_object(id)
        if isinstance(genre, Response) and genre.status_code == status.HTTP_404_NOT_FOUND:
            formatted_response = CommonResponse.get_formatted_response(
                message="Genre details not found.", success=False, response_data={}
            )
            return Response(data=formatted_response, status=status.HTTP_404_NOT_FOUND)
        genre_serializer = GenreSerializer(genre, data=request.data)

        if genre_serializer.is_valid():
            if is_genre_exist(name=request.data["name"]):
                '''
                Check if genre already exist.
                Response accordingly
                '''
                formatted_response = CommonResponse.get_formatted_response(
                    success=False, response_data={},
                    message="Genre name already exist.")
                return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)
            '''
            Update data if no duplicates & valid data.
            '''
            genre_serializer.save()
            formatted_response = CommonResponse.get_formatted_response(
                success=True, response_data=genre_serializer.data,
                message="Genre details updated successfully.")
            return Response(formatted_response, status=status.HTTP_202_ACCEPTED)
        formatted_response = CommonResponse.get_formatted_response(
            success=False, response_data={},
            message=genre_serializer.errors)
        return Response(data=formatted_response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        genre = get_object(id)
        if isinstance(genre, Response) and genre.status_code == status.HTTP_404_NOT_FOUND:
            formatted_response = CommonResponse.get_formatted_response(
                message="Genre details not found.", success=False, response_data={}
            )
            return Response(data=formatted_response, status=status.HTTP_404_NOT_FOUND)
        genre.delete()
        formatted_response = CommonResponse.get_formatted_response(
            message="Genre deleted successfully.", success=False, response_data={}
        )
        return Response(data=formatted_response, status=status.HTTP_204_NO_CONTENT)
