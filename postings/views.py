import json
from wsgiref.util import request_uri

from django.http import JsonResponse
from django.views import View


# class PostView(View) :
#     def post(self, request):
#         try :
#             data = json.loads(request.body)

#             return JsonResponse({"message": "POSTED"}, status=200)
#         except :
#             return JsonResponse({"message": "ERRORRRRRR"}, status=400)

#     def get(self, request):
#         try :
#             data = json.loads(request.body)
        
#             return JsonResponse({"message": "POSTED"}, status=200)
#         except :
#             return JsonResponse({"message": "ERRORRRRRR"}, status=400)



            
