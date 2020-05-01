from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from movies.many_to_many_api import GenreAPIView, ContentAPIView

router = DefaultRouter()
router.register('genre', GenreAPIView, basename='genre')
router.register('content', ContentAPIView)
urlpatterns = [

    path('', include(router.urls)),
    url('genre/get_content_by_genre', GenreAPIView.as_view, name='get_content_by_genre'),
    url('genre/get_genre_detail', GenreAPIView.as_view, name='get_genre_detail'),
]
