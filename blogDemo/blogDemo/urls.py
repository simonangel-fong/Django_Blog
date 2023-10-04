
from django.contrib import admin
from django.urls import path, include
from .views import HomeView, AboutView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path('admin/', admin.site.urls),
    path("blog/", include("AppBlog.urls")),
    path("accounts/", include("AppAccount.urls")),
]
