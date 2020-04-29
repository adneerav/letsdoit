from django.urls import path

# from .views import GenreAPI
from .class_api_view import GenreDetailAPIView
from .class_api_view_generic import GenreGenericAPIView

urlpatterns = [
    # url(r'^genre/?$', GenreAPIView.as_view()),  # for class base api view
    path('detail/<int:id>/', GenreDetailAPIView.as_view()),  # for class base api view
    path('genre/gendetail/<int:id>/', GenreGenericAPIView.as_view())

]
