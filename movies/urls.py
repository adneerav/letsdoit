from django.conf.urls import url
from django.urls import path

from . import views

# from .views import GenreAPI

urlpatterns = [
    # url(r'^content/?$', ContentAPI.as_view()),
    url(r'^genre/?$', views.article_list),
    path('detail/<int:pk>/', views.genre_detail)
]
