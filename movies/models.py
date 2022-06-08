from django.db import models

# Create your models here.

class Movie(models.Model) :
  title        = models.CharField(max_length=45)
  release_date = models.DateField()
  running_time_min = models.IntegerField(null=True)

  class Meta: 
    db_table = "movies"

class Actor(models.Model) :
  first_name    = models.CharField(max_length=45)
  last_name     = models.CharField(max_length=45)
  date_of_birth = models.DateField()

  class Meta : 
    db_table = "actors"


class MovieActor(models.Model) :
  actor = models.ForeignKey("Actor", on_delete=models.CASCADE)
  movie = models.ForeignKey("Movie", on_delete=models.CASCADE)

  class Meta :
    db_table = "movies_actors"