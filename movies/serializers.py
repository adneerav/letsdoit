from rest_framework import serializers

from movies.models import Content, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')
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
