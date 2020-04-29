from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from movies.many_to_many_api import GenreAPIView, ContentAPIView

router = routers.DefaultRouter()
router.register('genre', GenreAPIView)
router.register('content', ContentAPIView)
urlpatterns = [

    path('', include(router.urls))
    # url(r'^content/?$', ContentAPI.as_view()),

    # url(r'^genre/?$', fun_api_view_decorator.genre_list), # for function base api view
    # path('detail/<int:pk>/', fun_api_view_decorator.genre_detail) # for function base api view

    # url(r'^genre/?$', GenreAPIView.as_view()),  # for class base api view
    # path('detail/<int:id>/', GenreDetailAPIView.as_view()),  # for class base api view
    # path('genre/gendetail/<int:id>/', GenreGenericAPIView.as_view()),
    # path('api-token-auth/', AuthTokenAPIView.as_view()),

]
