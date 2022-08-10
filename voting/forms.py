from logging import PlaceHolder
from turtle import title
from django import forms
from .models import Creation, VotingList
from django.forms import ModelForm
from django.db import models


class CreationForm(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
    creator = forms.CharField(max_length=200)
    # image = forms.ImageField()


class VotingFormOLD(forms.Form):

    # choices for the radiobuttons (stars/ legobricks) in the voting form, (value, name)
    CHOICES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]

    vote = forms.ChoiceField(
        choices=CHOICES, widget=forms.RadioSelect, initial='1')

    # vote = forms.IntegerField()

    creationId = forms.CharField(widget=forms.HiddenInput(), required=True)


# https://stackoverflow.com/questions/14660037/django-forms-pass-parameter-to-form


class VotingForm(ModelForm):
    class Meta:
        model = VotingList
        fields = ['vote', 'creation']
        widgets = {'vote': forms.RadioSelect(choices=VotingList.CHOICES)}

    # def __init__(self, *args, **kwargs):
    #     super(VotingForm, self).__init__(*args, **kwargs)
    #     self.fields['vote'].choices = VotingList.CHOICES
