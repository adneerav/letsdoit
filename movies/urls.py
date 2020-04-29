from django.conf.urls import url
from django.urls import path

# from .views import GenreAPI
from movies import views

urlpatterns = [
    path('genre/detail/<int:pk>/', views.genre_detail),  # for function base api view
    url(r'^genre/?$', views.genre_list)  # for function base api view
]
