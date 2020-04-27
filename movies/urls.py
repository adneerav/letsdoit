from django.conf.urls import url
from django.urls import path

from . import views, fun_api_view_decorator

# from .views import GenreAPI
from .class_api_view import GenreAPIView, GenreDetailAPIView
from .class_api_view_generic import GenreGenericAPIView

urlpatterns = [
    # url(r'^content/?$', ContentAPI.as_view()),

    # url(r'^genre/?$', fun_api_view_decorator.genre_list), # for function base api view
    # path('detail/<int:pk>/', fun_api_view_decorator.genre_detail) # for function base api view

    # url(r'^genre/?$', GenreAPIView.as_view()),  # for class base api view
    path('detail/<int:id>/', GenreDetailAPIView.as_view()),  # for class base api view
    path('genre/gendetail/<int:id>/', GenreGenericAPIView.as_view())

]
