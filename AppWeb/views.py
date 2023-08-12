from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = "AppWeb/index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Home"
        context["heading"] = "Home"
        return context


class AboutView(TemplateView):
    template_name = "AppWeb/about.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "About"
        context["heading"] = "About"
        return context


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('AppWeb:home')
    template_name = 'account/signup.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Sign up"
        context["heading"] = "Sign up"
        return context


class LoginView(auth_views.LoginView):

    template_name = 'account/login.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Login"
        context["heading"] = "Login"
        return context


class ProfileView(TemplateView):
    template_name = "account/profile.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "User profile"
        context["heading"] = "User profile"
        return context
