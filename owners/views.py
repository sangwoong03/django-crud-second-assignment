from django.shortcuts import render

# Create your views here.
import json

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnerList(View):
  def post(self, request):
    data        = json.loads(request.body)
    
    owner_name  = data["name"]
    owner_email = data["email"]
    owner_age   = data["age"]
    

    Owner.objects.create(
        name  = owner_name,
        email = owner_email,
        age   = owner_age
    )

    return JsonResponse({'messasge':'주인 정보가 등록되었습니다.'}, status=201)

class DogList(View):
  def post(self, request):
    data      = json.loads(request.body)
    
    dog_name  = data["name"]
    dog_age   = data["age"]
    owner     = data["owner_id"] #Owner.objects.get(name=data["owner"])도 가능

    Dog.objects.create(
        name     = dog_name,
        age      = dog_age,
        owner_id = owner
    )

    return JsonResponse({'messasge':'강아지 정보가 등록되었습니다.'}, status=201)