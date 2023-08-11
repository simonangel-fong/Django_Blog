from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
from .models import Post


class BlogListView(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Post List"
        context["heading"] = "Post List"
        return context


class BlogDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Post Detail"
        context["heading"] = "Post Detail"
        return context


class BlogCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('AppBlog:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Post Add"
        context["heading"] = "Post Add"
        # context["form"] = PostForm
        return context


class BlogUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('AppBlog:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Post Add"
        context["heading"] = "Post Add"
        return context


class BlogDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('AppBlog:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Post Delete"
        context["heading"] = "Post Delete"
        return context
