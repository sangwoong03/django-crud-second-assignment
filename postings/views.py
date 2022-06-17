import json
from lib2to3.pgen2 import token

from django.http import JsonResponse
from django.views import View

from users.models import User
from .models import Post, Image

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
            return JsonResponse({"message": "ERRORRRRRR"}, status=400)

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
    # @token_decorator
    def get(self, request,user_id):
        try:
            # user = request.user
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
        
        except :
            return JsonResponse({"message" : "INVALID_USER"}, status=404)