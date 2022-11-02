from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'voting'  # here for namespacing of urls.

urlpatterns = [
    #     path("", views.votingHomepage, name="votingHomepage"),

    path("", views.login_request, name="login"),
    # no need for a 'homepage, only login and myvotes are needed, the navbar will change from logo to dashboard link if user is staff
    # TODO: remove logout view, only use as function?
    # see: https://www.squarefree.com/securitytips/web-developers.html#CSRF:~:text=Log%20the%20victim%20out%20of%20your%20site.%20(On%20some%20sites%2C%20%22Log%20out%22%20is%20a%20link%20rather%20than%20a%20button!)
    #     path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("myvotes/", views.myVotes, name="myvotes"),

    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/addcreation/", views.addCreation, name="addcreation"),
    path('edit/<int:pk>/',
         views.CreationUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/',
         views.CreationDeleteView.as_view(), name='delete'),
    path("dashboard/stats/", views.stats, name="stats"),
    path("dashboard/allcreations/", views.allCreations, name="allcreations"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
