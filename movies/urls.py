from django.conf.urls import url
from django.urls import path

# from .views import GenreAPI
from rest_framework.authtoken import views

from .auth_token_view import AuthTokenAPIView
from .class_api_view import GenreDetailAPIView
from .class_api_view_generic import GenreGenericAPIView

urlpatterns = [
    # url(r'^content/?$', ContentAPI.as_view()),

    # url(r'^genre/?$', fun_api_view_decorator.genre_list), # for function base api view
    # path('detail/<int:pk>/', fun_api_view_decorator.genre_detail) # for function base api view

    # url(r'^genre/?$', GenreAPIView.as_view()),  # for class base api view
    path('detail/<int:id>/', GenreDetailAPIView.as_view()),  # for class base api view
    path('genre/gendetail/<int:id>/', GenreGenericAPIView.as_view()),
    path('api-token-auth/', AuthTokenAPIView.as_view()),

]
