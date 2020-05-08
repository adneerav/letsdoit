from rest_framework import serializers

from letsdoit import settings
from movies.models import Content, Genre, ContentImage


class GenreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Genre
        fields = ('id', 'name')
        # read_only_fields = ('contents',)
        # extra_kwargs = {'contents': {'required': False}}
        ''''
        defined keys in fields will be return in response.
        Use '__all__' to sending all fields of the model
        '''

        '''
        exclude = ('id',)
        as per name it will exclude id in response.
        But to use exclude fields should be declared(used)
        either fields or exclude
        '''


class ContentImageSerializer(serializers.ModelSerializer):
    content_image = ContentImage
    thumb = serializers.SerializerMethodField()

    class Meta:
        model = ContentImage
        fields = ('id', 'thumb', 'type', 'content', 'added_date', 'thumb')

    def get_thumb(self, content_image):
        request = self.context.get('request')
        if request is None:
            return content_image.thumb.url
        photo_url = content_image.thumb
        return request.build_absolute_uri(photo_url.url)


class ContentSerializer(serializers.ModelSerializer):
    genres = GenreSerializer
    images = ContentImageSerializer(read_only=True, many=True)

    class Meta:
        model = Content
        fields = ['id', 'name', 'plot', 'genres', 'images', 'type', 'added_date']
        extra_kwargs = {
            "name": {
                "error_messages": {
                    "required": "name required.",
                    "blank": "name can not be blank."
                }
            }
        }
