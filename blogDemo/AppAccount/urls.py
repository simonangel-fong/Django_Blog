from django.urls import path
from AppBlog import views
from .views import SignUpView, LoginView, ProfileView
from django.contrib.auth import views as auth_views


app_name = "AppAccount"

urlpatterns = [

    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
