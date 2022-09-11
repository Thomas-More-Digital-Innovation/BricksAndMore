from logging import PlaceHolder
from tkinter import HIDDEN
from turtle import title
from typing_extensions import Required
from django import forms
from .models import Creation, VotingList
from django.forms import ModelForm
from django.db import models


class CreationForm(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
    creator = forms.CharField(max_length=200)
    # image = forms.ImageField()


class VotingForm(forms.Form):

    # choices for the radiobuttons (stars/ legobricks) in the voting form, (value, name)
    CHOICES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]

    # user enters vote
    # vote = forms.ChoiceField(
    #     choices=CHOICES, widget=forms.RadioSelect)

    # user enters vote
    vote = forms.ChoiceField(choices=CHOICES,
                             widget=forms.RadioSelect(attrs={'onchange': 'actionform.submit();'}))

    # place to keep track of the creation
    creationId = forms.IntegerField(widget=forms.HiddenInput)
    # creationId = forms.IntegerField()


# class VotingFormMODELVERSION(ModelForm):
#     class Meta:
#         model = VotingList
#         fields = ['vote']
#         widgets = {'vote': forms.RadioSelect(choices=VotingList.CHOICES)}

#     # def __init__(self, *args, **kwargs):
#     #     super(VotingForm, self).__init__(*args, **kwargs)
#     #     self.fields['vote'].choices = VotingList.CHOICES
