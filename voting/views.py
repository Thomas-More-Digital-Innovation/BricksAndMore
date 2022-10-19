from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.db.models import Avg, Min, Max, Count, Sum
from django.views.generic import UpdateView, DeleteView

from voting.forms import *
from voting.models import *

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
                          template_name="voting/register.html",
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

#############
# DASHBOARD #
#############


@ user_passes_test(lambda u: u.is_staff)
def dashboard(request):

    return render(request=request,
                  template_name="voting/dashboard.html",
                  context={"creations": Creation.objects.all()
                           })


@ user_passes_test(lambda u: u.is_staff)
def stats(request):
    # build a dictionary of the highest voted creations

    # dictionary of creation its avg vote regardless of category
    avgPerCreation = Creation.objects.annotate(
        avg=Avg("votinglist__vote")).order_by("-avg")
    # for i in range(len(avgPerCreation)):
    #     print(f"{avgPerCreation[i]}: {avgPerCreation[i].avg}")

    # dictionary of creation id and its avg vote per category
    highestCrea = Creation.objects.filter(votinglist__category__startswith="crea").annotate(
        avg=Avg("votinglist__vote")).order_by("-avg")

    # print(highestCrea)

    highestDeta = Creation.objects.filter(votinglist__category__startswith="deta").annotate(
        avg=Avg("votinglist__vote")).order_by("-avg")

    highestImpr = Creation.objects.filter(votinglist__category__startswith="impr").annotate(
        avg=Avg("votinglist__vote")).order_by("-avg")

    # amount of votes per creation
    amountOfVotes = Creation.objects.annotate(
        amount=Count("votinglist__vote")).order_by("-amount")

    # for i in range(len(amountOfVotes)):
    #     print(f"{amountOfVotes[i]}: {amountOfVotes[i].amount}")

    return render(request=request, template_name="voting/stats.html", context={
        "avgPerCreation": avgPerCreation,
        "highestCrea": highestCrea,
        "highestDeta": highestDeta,
        "highestImpr": highestImpr,
        "amountOfVotes": amountOfVotes,
        "creations": Creation.objects.all()})


@ user_passes_test(lambda u: u.is_staff)
def allCreations(request):
    return render(request=request, template_name="voting/allcreations.html", context={"creations": Creation.objects.all().order_by("number")})


# @ user_passes_test(lambda u: u.is_staff)
# def edit(request, creation_id):
#     creation = Creation.objects.get(id=creation_id)

#     if request.method == "POST":
#         form = CreationForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f"Creation updated added")
#             return redirect("voting:allcreations")
#         else:
#             for field, items in form.errors.items():
#                 for item in items:
#                     messages.error(request, '{}: {}'.format(field, item))

#         return render(request=request,
#                       template_name="voting:allcreations.html",
#                       context={"form": form})

#     form = CreationForm()

#     return render(request=request, template_name="voting/edit.html", context={"form": form, "creation": creation})

# TODO: change to class based view
@ user_passes_test(lambda u: u.is_staff)
def addCreation(request):
    # TODO: 404's if not superuser, change later to redirect to homepage maybe
    if request.method == "POST":
        form = CreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"New creation added")
            return redirect("voting:dashboard")
        else:
            for field, items in form.errors.items():
                for item in items:
                    messages.error(request, '{}: {}'.format(field, item))

        return render(request=request,
                      template_name="voting/addcreation.html",
                      context={"form": form})
    lastCreation = Creation.objects.last()

    form = CreationForm()
    return render(request=request,
                  template_name="voting/addcreation.html",
                  context={"form": form, 'lastCreation': lastCreation})


class CreationUpdateView(UpdateView):
    model = Creation
    form_class = CreationForm
    template_name = 'voting/edit.html'
    success_url = reverse_lazy('voting:allcreations')


class CreationDeleteView(DeleteView):
    model = Creation
    success_url = reverse_lazy('voting:allcreations')
    # template_name = reverse_lazy("voting:creation_delete_check.html")
