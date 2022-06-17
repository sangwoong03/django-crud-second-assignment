from django.db import models

from core.models import TimeStampModel
from users.models import User

class Post(TimeStampModel) :
    content = models.TextField()
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "posts"

class Image(TimeStampModel) :
    image_url = models.URLField(max_length=2000)
    post      = models.ForeignKey("POST", on_delete=models.CASCADE)

    class Meta:
        db_table = "images"