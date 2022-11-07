from ast import Attribute
from django import forms
from .models import Creation, VotingList
from django.forms import ModelForm
from django.db import models
from django.forms import ModelForm


class CreationForm(ModelForm):
    class Meta:
        model = Creation
        fields = ['number', 'name', 'description', 'creator', 'image']
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 50%; margin: 0 auto; margin-bottom: 10px; font-size: 3rem; font-weight: bold; color: #000; background-color: #fff;'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'style': 'width: 50%; margin: 0 auto; margin-bottom: 10px; font-size: 3rem; font-weight: bold; color: #000; background-color: #fff;'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'style': 'width: 50%; margin: 0 auto; margin-bottom: 10px; font-size: 3rem; font-weight: bold; color: #000; background-color: #fff;'}),
            'creator': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'style': 'width: 50%; margin: 0 auto; margin-bottom: 10px; font-size: 3rem; font-weight: bold; color: #000; background-color: #fff;'}),
            'image': forms.FileInput(attrs={'accept': 'image/*', 'capture': 'camera'})



            # 'number': forms.NumberInput(widget=forms.IntegerField(attrs={'class': 'form-control'})),
            # 'name': forms.TextInput(widget=forms.TextInput(attrs={'class': 'form-control'})),
            # 'description': forms.TextInput(widget=forms.TextInput(attrs={'class': 'form-control'})),
            # 'creator': forms.TextInput(widget=forms.TextInput(attrs={'class': 'form-control'})),
            # 'image': forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'})),
        }
# class CreationForm(forms.Form):
#     name = forms.CharField(max_length=200)
#     description = forms.CharField(max_length=200)
#     creator = forms.CharField(max_length=200)
#     image = forms.ImageField(required=False)


class VotingForm(forms.Form):

    # choices for the radiobuttons (stars/ legobricks) in the voting form, (value, name)
    # CHOICES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]

    # user enters vote
    vote = forms.ChoiceField(
        choices=VotingList.CHOICES, widget=forms.RadioSelect, required=False)

    # user enters vote (submits on change)
    # vote = forms.ChoiceField(choices=CHOICES,
    #                          widget=forms.RadioSelect(attrs={'onchange': 'actionform.submit();'}), required=FALSE)

    # place to keep track of the creation
    creationId = forms.IntegerField(widget=forms.HiddenInput)
    category = forms.CharField(max_length=20, widget=forms.HiddenInput)
    # creationId = forms.IntegerField()
