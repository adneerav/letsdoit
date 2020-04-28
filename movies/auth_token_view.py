from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django_expiring_token.authentication import ExpiringToken
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import APIException
from rest_framework.response import Response


class AuthTokenAPIView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data,
                                               context={'request': request})
            serializer.is_valid(raise_exception=True)
            '''
            default django user model & serializer will be accessed 
            '''
            user = serializer.validated_data['user']
            '''
            Token is default django Model class from rest_framework.authtoken
            by passing user model token can be get & create if not generated.  
            '''
            token, created = ExpiringToken.objects.get_or_create(user=user)
        except APIException as e:
            return Response({
                "success": False,
                "message": e.detail
            }, status=e.status_code)
        return Response({
            'token': token.key,
            'token_created_time': token.created,
            'token_expires_time': token.expires,
            'token_created_ms': datetime.timestamp(token.created),
            'token_expires_ms': datetime.timestamp(token.expires),
            'user_id': user.pk,
            'email': user.email
        })

    '''
    To delete generated auth token.
    use case can be : delete token at the time of logout.
    '''

    def delete(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        try:
            user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"success": True,
                         "message": "Token removed successfully."}
                        , status=status.HTTP_204_NO_CONTENT)
