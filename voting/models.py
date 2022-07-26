from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from bricks import settings
# Create your models here.


class Creation(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='creations/')
    number = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class VotingList(models.Model):
    CHOICES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
    # add one-to-one relationship with user
    # user = models.OneToOneField(
    # User, on_delete=models.CASCADE, primary_key=True)

    # add many-to-one relationship with user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # add many-to-many relationship with Creation
    creation = models.ManyToManyField(Creation)

    CATEGORIES = ["creativiteit", "details", "indrukwekkend"]
    category = models.CharField(max_length=20)

    vote = models.IntegerField(blank=True, null=True)
