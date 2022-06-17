from django.urls import path

from postings.views import PostView, PostSearchView

urlpatterns = [
    path("", PostView.as_view()),
    path("/search/<int:user_id>", PostSearchView.as_view())
]
