from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import *
from .forms import *

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
            vote = form.cleaned_data.get('vote')
            creationId = form.cleaned_data.get('creationId')
            creation = Creation.objects.get(id=creationId)
            user = request.user
            print(f"formstuff: {vote, creationId, user}")

            # if user does not have a VotingList, create one and add the vote
            if not VotingList.objects.filter(user=user, creation=Creation.objects.get(id=creationId)).exists():

                print("no voting list")

                newVotingList = VotingList(user=user,
                                           vote=vote)
                for member in creation.iterator():
                    newVotingList.add(member)
                # userVotingList = VotingList.objects.add(
                #     user=user,
                #     creation=Creation.objects.get(id=creationId),
                #     vote=vote
                # )
                print(f"userVotingList: {newVotingList}")
            # print("found votingList")
            # except:  # userVotingList.DoesNotExist
            #     print("creating votingList (to be implemented)")
            # votingList = VotingList(user=user)
            # votingList.save()
            # print("saved votingList")

            print("\nSUBMITTED:")
            print(f"vote: {vote}, user: {user}, creationId: {creationId}\n")

        else:
            print("invalid form")
            # creation = Creation.objects.get(id=crea)

           # need: USER, CREATION, VOTE
           # get the user's voting list if exist => update the vote
           # else create a new voting list with the vote and the creation  and user as fk's

           # get the user's voting list if exist
           # if votingList where creation = submittedcreation exists:
           # votingList.vote = vote
           # else
           # VotingList.objects.create(user=request.user, creation=submittedcreation, vote=vote)

           # messages.success(request, f"New creation added: {name}")
        return redirect("voting:myvotes")
        # else:
        #     for msg in form.error_messages:
        #         messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = VotingForm()
    return render(request=request,
                  template_name="voting/myvotes.html",
                  context={"form": form, "creations": Creation.objects.all(), "votingList": VotingList.objects.all()})


def userIsStaff(user):
    return user.is_staff
    # TODO: does this even work? shouldn't the lambda below be u.userIsStaff()?


@ user_passes_test(lambda u: u.is_staff)
def dashboard(request):
    return render(request=request,
                  template_name="voting/dashboard.html",
                  context={"creations": Creation.objects.all()})


@ user_passes_test(lambda u: u.is_staff)
def addCreation(request):
    # 404's if not superuser, change later to redirect to homepage maybe
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
