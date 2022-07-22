from django import forms


class CreationForm(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
    creator = forms.CharField(max_length=200)
    # image = forms.ImageField()
