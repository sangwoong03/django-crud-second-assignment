from django.db import models

class TimeStampModel(models.Model):
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    class Meta :
        abstract = True