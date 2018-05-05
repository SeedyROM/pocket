import os

from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_altered = models.DateTimeField(blank=True, null=True)

    def attributes(self):
        return self.__dict__

    class Meta:
        abstract = True
        app_label = os.path.dirname(__file__).split('/')[-1]


class User(BaseModel):
    username = models.CharField(max_length=32, unique=True, primary_key=True)
    password = models.CharField(max_length=512)