from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import UserSerializer, RegistrationSerializer


class UserRegistration(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        print(serializer)
        print(serializer.is_valid(raise_exception=True))
        serializer.save()
        success = True if serializer.is_valid(raise_exception=True) else False
        return Response({"success": success}, status=status.HTTP_200_OK)