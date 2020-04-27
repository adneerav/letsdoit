from django.conf.urls import url

from . import views
# from .views import GenreAPI

urlpatterns = [
    # url(r'^content/?$', ContentAPI.as_view()),
    url(r'^genre/?$', views.article_list)
]
