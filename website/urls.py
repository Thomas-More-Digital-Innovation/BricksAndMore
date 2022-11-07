from allauth.account.views import LoginView, SignupView
from django.urls import path, include
from . import views
from voting import views as voting_views


app_name = 'website'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    # Bypass the Django allauth login view and use the custom one
    path('accounts/login/', voting_views.login_request, name="custom_login"),
    path('accounts/signup/', voting_views.login_request, name="custom_singup"),
]
