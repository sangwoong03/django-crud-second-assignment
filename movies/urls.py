from django.urls import path

from .views import ActorList, MovieList

urlpatterns = [
    path('/movie', MovieList.as_view()),
    path('/actor', ActorList.as_view()),
]