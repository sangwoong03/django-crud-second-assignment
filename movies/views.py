from django.shortcuts import render

# Create your views here.
import json

from django.http import JsonResponse
from django.views import View

from movies.models import Movie, Actor, MovieActor

class MovieList(View):

  def get(self, request):
    movies  = Movie.objects.all();
    results = [
      {
        "제목"   : movie.title,
        "상영시간": f"{movie.running_time_min}분",
        "출연배우": [movie_actor.actor.last_name + movie_actor.actor.first_name for movie_actor in MovieActor.objects.filter(movie_id=movie.id)]
      } for movie in movies
    ]
  
    return JsonResponse({"영화 정보": results }, status=200)

class ActorList(View):
  
  def get(self, request):
    actors  = Actor.objects.all()
    results = [
      {
        "이름": actor.last_name + actor.first_name,
        "출연작": [movie_actor.movie.title for movie_actor in MovieActor.objects.filter(actor_id=actor.id)]
      } for actor in actors
    ]
    

    return JsonResponse({"배우 정보": results}, status=200)

