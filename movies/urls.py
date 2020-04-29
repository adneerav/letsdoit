from django.conf.urls import url
from django.urls import path

from . import fun_api_view_decorator

urlpatterns = [
    url(r'^genre/?$', fun_api_view_decorator.genre_list),  # for function base api view decorator
    path('genre/<int:pk>/', fun_api_view_decorator.genre_detail)  # for function base api view decorator
]
