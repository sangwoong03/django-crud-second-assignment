from django.urls import path

from .views import ActorView, MovieView
urlpatterns = [
    path('/movie', MovieView.as_view()),
    path('/actor', ActorView.as_view()),
]