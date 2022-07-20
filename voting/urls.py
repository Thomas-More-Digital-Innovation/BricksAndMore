from django.urls import path, include
from . import views


app_name = 'voting'  # here for namespacing of urls.

urlpatterns = [
    path("", views.votingHomepage, name="votingHomepage"),
    # TODO: remove logout view, only use as function?
    # see: https://www.squarefree.com/securitytips/web-developers.html#CSRF:~:text=Log%20the%20victim%20out%20of%20your%20site.%20(On%20some%20sites%2C%20%22Log%20out%22%20is%20a%20link%20rather%20than%20a%20button!)
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("myvotes/", views.myVotes, name="myvotes"),
]
