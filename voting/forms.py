from django import forms


class CreationForm(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
    creator = forms.CharField(max_length=200)
    # image = forms.ImageField()


class VotingForm(forms.Form):
    vote = forms.IntegerField()
    creationId = forms.CharField(widget=forms.HiddenInput(), required=True)


# https://stackoverflow.com/questions/14660037/django-forms-pass-parameter-to-form
