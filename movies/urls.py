from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewset_api_view import GenreViewSet, GenreSecondViewSet

router = DefaultRouter()
router.register('genre', GenreViewSet, basename='genre')
'''
Below register viewset in router to test multiple api viewset in api root
'''
router.register('genre_clone', GenreSecondViewSet, basename='clone')

urlpatterns = [
    path('', include(router.urls)),
]
