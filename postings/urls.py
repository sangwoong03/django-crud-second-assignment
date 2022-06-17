from django.urls import path

from postings.views import PostView, PostSearchView, CommentView, CommentSearchView

urlpatterns = [
    path("", PostView.as_view()),
    path("/search/<int:user_id>", PostSearchView.as_view()),
    path("/comment", CommentView.as_view()),
    path("/comment/search/<int:post_id>", CommentSearchView.as_view()),
]
