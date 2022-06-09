from django.shortcuts import render

# Create your views here.
import json

from django.http import JsonResponse
from django.views import View

from movies.models import Movie, Actor

class MovieList(View):

  def get(self, request):
    movies  = Movie.objects.all()
    results = []

    for movie in movies :
      title   = movie.title
      runtime = movie.running_time_min

      results.append(
        {
          "제목": title,
          "상영시간": runtime,
          "출연진" : [actor.last_name + actor.first_name for actor in movie.actors.all()]
        }
      )
  
    return JsonResponse({"영화 정보": results }, status=200)

class ActorList(View):
  
  def get(self, request):
    actors  = Actor.objects.all()
    results = []

    for actor in actors :
      name   = actor.last_name + actor.first_name

      results.append(
        {
          "이름": name,
          "출연작": [movie.title for movie in actor.movie_set.all()]
        }
      )
    

    return JsonResponse({"배우 정보": results}, status=200)

