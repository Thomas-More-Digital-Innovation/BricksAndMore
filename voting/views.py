from audioop import avg
from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Avg, Min, Max, Count, Sum

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
        if form.is_valid():
            user = request.user
            creationId = form.cleaned_data.get('creationId')
            category = form.cleaned_data.get('category')
            vote = form.cleaned_data.get('vote')
            print(
                f"creationID: {creationId} category: {category}, voteValue: {vote}")

            # if user does not have a VotingList, create one and add the vote
            if not VotingList.objects.filter(user=user, creation=Creation.objects.get(id=creationId), category=category).exists():
                # if not VotingList.objects.filter(user=user, creation=creation).exists():
                votedCreation = Creation.objects.get(id=creationId)
                # print(f"___votedCreation: {votedCreation}")

                newVotingList = VotingList(user=user,
                                           vote=vote,
                                           category=category,
                                           )
                newVotingList.save()
                newVotingList.creation.set([votedCreation])

            # if user does have a VotingList, add the vote to the list
            # TODO: change to else?
            elif VotingList.objects.filter(user=user, creation=Creation.objects.get(id=creationId), category=category).exists():
                # elif VotingList.objects.filter(user=user, creation=creation).exists():
                updateVotingList = VotingList.objects.get(
                    user=user, creation=Creation.objects.get(id=creationId), category=category)
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

        # formList contains all forms and needed values
        formList = []
        for creation in Creation.objects.all():
            # formListItems contains each individual creation, form and vote if there is one
            # {'creation': creation, 'forms': {creativity: form(), uniqueness: form(), impressiveness: form()}, 'vote': currentvote}
            formListItems = {}
            # add the creation to the formListItems dictionary
            formListItems['creation'] = creation

            categoryForms = {}
            for category in VotingList.CATEGORIES:
                if VotingList.objects.filter(
                        user=request.user,
                        creation=Creation.objects.get(id=creation.id), category=category).exists():
                    # get the vote
                    currentVote = VotingList.objects.filter(
                        user=request.user, creation=Creation.objects.get(id=creation.id), category=category).get().vote
                else:
                    currentVote = None

                # add the current vote for that category to the formListItems
                categoryForm = {"form": VotingForm(), "vote": currentVote}
                categoryForms[category] = categoryForm
            formListItems['categoryForms'] = categoryForms
            formList.append(formListItems)

        return render(request=request,
                      template_name="voting/myvotes.html",
                      context={
                          "formList": formList,
                          # "creations": Creation.objects.all(),
                          "votingLists": VotingList.objects.filter(user_id=request.user.id)
                      })


def userIsStaff(user):
    return user.is_staff


@ user_passes_test(lambda u: u.is_staff)
def dashboard(request):
    # build a dictionary of the highest voted creations

    # dictionary of creation its avg vote regardless of category
    avgPerCreation = Creation.objects.annotate(
        avg=Avg("votinglist__vote")).order_by("-avg")
    # for i in range(len(avgPerCreation)):
    #     print(f"{avgPerCreation[i]}: {avgPerCreation[i].avg}")

    # dictionary of creation id and its avg vote per category
    Creation.objects.values('id').annotate(avg=Avg("votinglist__vote"))

    highestCrea = VotingList.objects.filter(
        category__startswith="crea").aggregate(avg=Avg("vote"))
    print(highestCrea)

    highestUniq = VotingList.objects.filter(
        category__startswith="uniq").aggregate(avg=Avg("vote"))

    highestImpr = VotingList.objects.filter(
        category__startswith="impr").aggregate(avg=Avg("vote"))

    return render(request=request,
                  template_name="voting/dashboard.html",
                  context={
                      "avgPerCreation": avgPerCreation,
                      "highestCrea": highestCrea,
                      "highestUniq": highestUniq,
                      "highestImpr": highestImpr,
                      "creations": Creation.objects.all()
                  })


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
