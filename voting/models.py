from django.db import models

# Create your models here.


class Creation(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    # image = models # TODO: https://www.geeksforgeeks.org/imagefield-django-models/ ?
    creator = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# TODO: VotingList
# TODO: link VotingList to user
