from django.urls import path
from .views import HomeView, AboutView, SignUpView, LoginView, ProfileView
from django.contrib.auth import views as auth_views

app_name = "AppWeb"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),

    path("accounts/signup/", SignUpView.as_view(), name="signup"),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/profile/", ProfileView.as_view(), name="profile"),
]
