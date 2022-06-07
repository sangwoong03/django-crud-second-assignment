from django.urls import path

from .views import OwnerList, DogList

urlpatterns = [
    path('', OwnerList.as_view()),
    path('dogs', DogList.as_view()),
]