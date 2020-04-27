from django.conf.urls import url
from django.urls import path

from . import views, fun_api_view_decorator

# from .views import GenreAPI

urlpatterns = [
    # url(r'^content/?$', ContentAPI.as_view()),
    url(r'^genre/?$', fun_api_view_decorator.genre_list),
    path('detail/<int:pk>/', fun_api_view_decorator.genre_detail)
]
