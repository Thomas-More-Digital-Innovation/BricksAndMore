from django.db import models

# Create your models here.


class TutorialCategory(models.Model):

    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category


class Creation(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    # image = models # TODO: https://www.geeksforgeeks.org/imagefield-django-models/ ?
    creator = models.CharField(max_length=200)

# Leftoff: create page to add creations to test model functionality, should later only be accessible by group staff or w/ever

# TODO: VotingList
# TODO: link VotingList to user
