from django.urls import path

from .views import ActorList, MovieList

urlpatterns = [
    path('', MovieList.as_view()),
    path('/actors', ActorList.as_view()),
]