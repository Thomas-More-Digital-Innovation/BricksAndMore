from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from bricks import settings
# Create your models here.


class Creation(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    # image = models # TODO: https://www.geeksforgeeks.org/imagefield-django-models/ ?
    creator = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class VotingList(models.Model):
    # add one-to-one relationship with user
    # user = models.OneToOneField(
    # User, on_delete=models.CASCADE, primary_key=True)

    # add many-to-one relationship with user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # add many-to-many relationship with Creation
    creation = models.ManyToManyField(Creation)

    vote = models.IntegerField(blank=True, null=True)
