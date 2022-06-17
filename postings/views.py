import json

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
        try :
            data = json.loads(request.body)
        
            return JsonResponse({"message": "POSTED"}, status=200)
        except :
            return JsonResponse({"message": "ERRORRRRRR"}, status=400)



            
