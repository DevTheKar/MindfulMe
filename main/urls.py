from django.urls import path
from . import views
import django.contrib.auth.views as auth_views

urlpatterns = [
    #Default links
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
   
    #Journal
    path("journal/", views.journal, name='journal'),

    #Spotify
    #path("spotify/", views.spotify, name="spotify"),

    #Register
    path('signup/', views.signup, name='signup'),

    #Login
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),

    #affirm
    path('affirm/', views.affirm, name='affirm'),

    #track
    path('track/', views.track, name="track")
]