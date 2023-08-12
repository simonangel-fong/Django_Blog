from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
from .models import Post


class BlogListView(ListView):
    ''' Blog list view '''
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Post List"
        context["heading"] = "Post List"
        return context


class BlogDetailView(DetailView):
    ''' Blog detail view '''

    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Post Detail"
        context["heading"] = "Post Detail"
        return context


class BlogCreateView(LoginRequiredMixin, CreateView):
    ''' Blog Create View '''
    model = Post
    form_class = PostForm       # The form class to instantiate.
    # The URL to redirect to when the form is successfully processed.
    success_url = reverse_lazy('AppBlog:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Post"
        context["heading"] = "New Post"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        form.save()
        return super(BlogCreateView, self).form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Post Add"
        context["heading"] = "Post Add"
        return context

    # Sets the URL to redirect to when the form is successfully processed.
    def get_success_url(self):
        return reverse_lazy('AppBlog:detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('AppBlog:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Post Delete"
        context["heading"] = "Post Delete"
        return context
