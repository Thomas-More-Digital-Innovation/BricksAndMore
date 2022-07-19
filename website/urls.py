from django.urls import path, include
from . import views


app_name = 'website'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
]
