from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import *

urlpatterns = [

    path('users/register/', register, name="register"),

    path('users/profile/', profile, name="profile"),

    path('users/login/',
         auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),

    path('users/logout/', auth_views.LogoutView.as_view(
        template_name="users/logout.html"), name="logout"),
]
