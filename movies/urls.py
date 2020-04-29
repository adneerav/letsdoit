from django.conf.urls import url
from django.urls import path

# from .views import GenreAPI
from rest_framework.authtoken import views

from . import fun_api_view_decorator
from .auth_token_view import AuthTokenAPIView
from .class_api_view_generic import GenreGenericAPIView

urlpatterns = [
    url(r'^genre_fun_auth/?$', fun_api_view_decorator.genre_list),  # for function base api view
    path('genre_fun_auth/detail/<int:pk>/', fun_api_view_decorator.genre_detail),  # for function base api view

    path('genre/generic_detail/<int:id>/', GenreGenericAPIView.as_view()),
    path('api-token-auth/', AuthTokenAPIView.as_view()),

]
