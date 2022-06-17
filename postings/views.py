from ast import JoinedStr
import json

from django.http import JsonResponse
from django.views import View

from users.models import User
from .models import Post, Image, Comment

from users.utils import token_decorator

class PostView(View) :
    @token_decorator
    def post(self, request):
        try :
            data = json.loads(request.body)
            user = request.user
            
            content    = data["content"]
            image_urls = data["image_url"]
            
            post = Post.objects.create(
                content   = content,
                user      = user,
            )

            for image_url in image_urls :
                Image.objects.create(
                    image_url = image_url,
                    post      = post   
                )

            return JsonResponse({"message": "POSTED"}, status=200)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

    def get(self, request):
        post_list = [
            {
                "account"      : User.objects.get(id=post.user.id).account,
                "content"      : post.content,
                "image_url"    : [image.image_url for image in Image.objects.filter(post_id = post.id)],
                "created_date" : post.created_at
            } for post in Post.objects.all()
        ]
        return JsonResponse({"data" : post_list}, status=200)

class PostSearchView(View) :
    def get(self, request,user_id):
        try:
            user = User.objects.get(id = user_id)
            post_list = [
                {
                    "account"      : user.account,
                    "content"      : post.content,
                    "image_url"    : [image.image_url for image in Image.objects.filter(post_id = post.id)],
                    "created_date" : post.created_at
                } for post in Post.objects.filter(user_id = user.id)
            ]
            
            return JsonResponse({"data" : post_list}, status=200)
        
        except User.DoesNotExist:
            return JsonResponse({"message" : "INVALID_USER"}, status=404)

class CommentView(View):
    @token_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            post = Post.objects.get(id=data["post"])
            user = request.user
            
            comment_contents = data["comment_content"]
            
            for comment_content in comment_contents :
                Comment.objects.create(
                    comment_content = comment_content,
                    post = post,
                    user = user
                )
            return JsonResponse({"message": "Comment Posted"}, status=201)
        except Post.DoesNotExist:
            return JsonResponse({"message": "INVALID_POST"}, status=400)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

    def get(self, request) :
        comments = Comment.objects.all()

        comment_list = [
            {
                "commet_content": comment.comment_content,
                "user"          : comment.user.account,
                "post"          : {
                    "content": comment.post.content
                }
            } for comment in comments
        ]
        return JsonResponse({"data": comment_list}, status=200)

class CommentSearchView(View): 
    def get(self, request, post_id) :
        try:
            post = Post.objects.get(id = post_id)

            comment_list = [
                {
                    "account"        : User.objects.get(id = comment.user.id).account,
                    "commet_content" : comment.comment_content,
                    "created_date"   : comment.created_at 
                } for comment in Comment.objects.filter(post_id = post.id)
            ]

            return JsonResponse({"data": comment_list}, status=200)
        
        except Post.DoesNotExist :
            return JsonResponse({"message": "INVALID_POST"})