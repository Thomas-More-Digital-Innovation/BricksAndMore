from django.db import models

# Create your models here.


class Creation(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    # image = models # TODO: https://www.geeksforgeeks.org/imagefield-django-models/ ?
    creator = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Leftoff: create page to add creations to test model functionality, should later only be accessible by group staff or w/ever

# TODO: VotingList
# TODO: link VotingList to user
