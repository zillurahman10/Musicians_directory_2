from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=100)
    musicians = models.ForeignKey(User, on_delete=models.CASCADE)
    release_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()

    def __str__(self) -> str:
        return self.title

    