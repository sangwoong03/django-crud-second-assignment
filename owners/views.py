from django.shortcuts import render

# Create your views here.
import json

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnerList(View):
		def post(self, request) :
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

		def get(self, request) :
			owners  = Owner.objects.all()
			results = []

			for owner in owners :
				dog_list = [
					{
						"이름": dog.name,
						"나이": dog.age
					} for dog in Dog.objects.filter(owner_id = owner.id)
				]
				
				results.append(
					{
						"이름"   : owner.name,
						"이메일" : owner.email,
						"나이"   : owner.age,
						"강아지" : dog_list
					}
				)
			
			return JsonResponse({'주인+강아지 리스트': results}, status=200)


class DogList(View):
		def post(self, request) :
			data      = json.loads(request.body)
			
			dog_name  = data["name"]
			dog_age   = data["age"]
			owner     = Owner.objects.get(name=data["owner"])

			Dog.objects.create(
					name  = dog_name,
					age   = dog_age,
					owner = owner
			)
			
			return JsonResponse({'messasge':'강아지 정보가 등록되었습니다.'}, status=201)

		def get(self, requeset) :
			dogs    = Dog.objects.all()
			results = []

			for dog in dogs :
				results.append(
					{
						"이름"     : dog.name,
						"나이"     : dog.age,
						"주인 이름" : dog.owner.name
					}
				)

			return JsonResponse({'강아지 정보': results}, status=200)