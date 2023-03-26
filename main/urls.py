from django.urls import path
from . import views
import django.contrib.auth.views as auth_views

app_name = 'main'

urlpatterns = [
    #Default links
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
   
    #Journal
    path("journal/", views.journal, name='home_page'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),

    #Spotify
    #path("spotify/", views.spotify, name="spotify"),

    #Register
    path('signup/', views.signup, name='signup'),

    #Login
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),

    #affirm
    path('affirm/', views.affirm, name='affirm'),

    #track
    path('track/', views.track, name="track"),

    

    #tracktest
    #trackcreatetest
    
    
    path("<int:id>", views.list, name="index"),

    path("create/", views.create, name="create"), # Create Lists

    path("view/", views.view, name="view"),
]