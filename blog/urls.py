from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='blog'

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='blog/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='blog/loggedout.html'),name='logout'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('create_profile/',views.ProfileCreationView.as_view(),name='create_profile'),
    path('profile/',views.UserProfileView.as_view(),name='user_profile')
]