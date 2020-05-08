from django.conf.urls import url
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from movies.content_api import ContentAPIView, ContentListView

from movies.content_image_api import ContentImageAPIView
from movies.genre_api import GenreDetail, GenreAPI

urlpatterns = [
    url(r'^genre/?$', GenreAPI.as_view()),  # genre list get & post api
    path('genre/<int:id>/', GenreDetail.as_view()),  # genre id wise get ,put & delete api
    path('content/<int:id>/', ContentAPIView.as_view()),
    path('contents/', ContentListView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('content/<int:content_id>/images/', ContentImageAPIView.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('content/image/<int:id>/', ContentImageAPIView.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
        'put': 'update',
    })),

    url(r'^auth/jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^auth/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
