from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import *
from .models import *

# Create your views here.


def votingHomepage(request):
    return render(request=request,
                  template_name='voting/votingHomepage.html',
                  context={}
                  )


def register(request):
    if request.method == "POST":
        print("POST")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            # TODO: login and route to myvotes
            # return redirect("voting:votingHomepage")
            return redirect("voting:myvotes")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request=request,
                          template_name="register",
                          context={"form": form})

    # elif request.method == "GET":
    form = UserCreationForm
    return render(request=request,
                  template_name="voting/register.html",
                  context={"form": form}
                  )


def login_request(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect('voting:myvotes')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('voting:myvotes')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="voting/login.html",
                  context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")  # TODO messages
    return redirect("website:homepage")


@login_required  # TODO add this
def myVotes(request):
    if request.method == "POST":
        print("POST")
        form = VotingForm(data=request.POST)
        print(f"formErrors: {form.errors}")
        voteValue = request.POST.get('vote')
        print(
            f"voteValue: {voteValue}, creationID: {request.POST.get('creationId')}")
        if form.is_valid():
            user = request.user
            creationId = form.cleaned_data.get('creationId')
            vote = form.cleaned_data.get('vote')
            # vote = form.cleaned_data.get('creation_' + str(creationId))
            # print(f"________ACTUAL_FORMSTUFF______: {form.cleaned_data}")
            # print(f"________FORMSTUFF______: {vote, creationId, user}")

            # if user does not have a VotingList, create one and add the vote
            if not VotingList.objects.filter(user=user, creation=Creation.objects.get(id=creationId)).exists():
                # if not VotingList.objects.filter(user=user, creation=creation).exists():
                votedCreation = Creation.objects.get(id=creationId)
                # print(f"___votedCreation: {votedCreation}")

                newVotingList = VotingList(user=user,
                                           vote=vote,
                                           )
                newVotingList.save()
                newVotingList.creation.set([votedCreation])

            # if user does have a VotingList, add the vote to the list
            # TODO: change to else?
            elif VotingList.objects.filter(user=user, creation=Creation.objects.get(id=creationId)).exists():
                # elif VotingList.objects.filter(user=user, creation=creation).exists():
                updateVotingList = VotingList.objects.get(
                    user=user, creation=Creation.objects.get(id=creationId))
                updateVotingList.vote = vote
                updateVotingList.save()

        else:
            print("invalid form")

        return redirect("voting:myvotes")
        # else:
        #     for msg in form.error_messages:
        #         messages.error(request, f"{msg}: {form.error_messages[msg]}")

    elif request.method == "GET":
        # make a dictionary of all creations and a form for them,
        # then add an attribute to fill in the current vote, if there is one, as an initial value
        formDict = {}
        for creation in Creation.objects.all():
            # if there is a vote in the corresponding VotingList
            if VotingList.objects.filter(user=request.user, creation=Creation.objects.get(id=creation.id)).exists():
                # get the vote
                currentVote = VotingList.objects.filter(
                    user=request.user, creation=Creation.objects.get(id=creation.id)).get().vote
                # add the current vote to the form
                print(f"currentVote: {currentVote}")
                form = VotingForm(
                    # initial={'vote': currentVote, 'creationId': creation.id} # initial values won't work with manually rendered forms
                )
            # if no vote is found
            else:
                form = VotingForm(
                    # initial={'vote': currentVote, 'creationId': creation.id} # initial values won't work with manually rendered forms
                )
            # add the form to the list of forms
            formDict[creation] = form
        print(f"formDict: {formDict}")

        return render(request=request,
                      template_name="voting/myvotes.html",
                      context={"formDict": formDict,
                               #    "creations": Creation.objects.all(),
                               "votingLists": VotingList.objects.filter(user_id=request.user.id)
                               })


def userIsStaff(user):
    return user.is_staff


@ user_passes_test(lambda u: u.is_staff)
def dashboard(request):
    return render(request=request,
                  template_name="voting/dashboard.html",
                  context={"creations": Creation.objects.all()})


@ user_passes_test(lambda u: u.is_staff)
def addCreation(request):
    # TODO: 404's if not superuser, change later to redirect to homepage maybe
    if request.method == "POST":
        form = CreationForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            creator = form.cleaned_data.get('creator')
            # image = form.cleaned_data.get('image')
            Creation.objects.create(
                name=name, description=description, creator=creator)
            messages.success(request, f"New creation added: {name}")
            return redirect("voting:dashboard")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

        return render(request=request,
                      template_name="voting/addcreation.html",
                      context={"form": form})

    form = CreationForm()
    return render(request=request,
                  template_name="voting/addcreation.html",
                  context={"form": form})
