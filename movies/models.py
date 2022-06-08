from django.db import models

# Create your models here.

class Movie(models.Model) :
  title            = models.CharField(max_length=45)
  release_date     = models.DateField()
  running_time_min = models.IntegerField(null=True)
  actor            = models.ManyToManyField("Actor", db_table="movie_actor")
  # 영화가 배우를 정참조 ↔ 배우는 영화를 역참조(_set)

  class Meta: 
    db_table = "movies"

class Actor(models.Model) :
  first_name    = models.CharField(max_length=45)
  last_name     = models.CharField(max_length=45)
  date_of_birth = models.DateField()

  class Meta : 
    db_table = "actors"