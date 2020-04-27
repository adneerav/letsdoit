from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('id', 'username', 'first_name', 'last_name', 'country_code',
                  'mobile', 'photo', 'gender', 'last_login', 'is_verified', 'birth_date',
                  'address_1', 'address_2')
        read_only_fields = ('last_login', 'is_active')


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'country_code',
                  'mobile', 'photo', 'gender', 'last_login', 'is_verified', 'birth_date',
                  'address_1', 'address_2')
        extra_kwargs = {'password': {'write_only': False},
                        'first_name': {'required': False},
                        'last_name': {'required': True}
                        }

    def to_internal_value(self, data):
        user_data = data.copy()
        country_code = data['country_code']
        mobile = data['mobile']
        user_data['username'] = '%s%s' % (country_code, mobile)
        return super(RegistrationSerializer, self).to_internal_value(user_data)

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'],
            country_code=validated_data['country_code'], mobile=validated_data['mobile'],
            first_name=validated_data['first_name'], last_name=validated_data['last_name'],
            is_active=False
        )
        return user
