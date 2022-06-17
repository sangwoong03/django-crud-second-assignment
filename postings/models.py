from django.db import models

from core.models import TimeStampModel
from users.models import User

class Posting(TimeStampModel) :
    content   = models.TextField()
    image_url = models.URLField(max_length=2000)
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "postings"