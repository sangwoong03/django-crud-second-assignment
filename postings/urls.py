from django.urls import path

from postings.views import PostView

urlpatterns = [
    path("", PostView.as_view())
]
