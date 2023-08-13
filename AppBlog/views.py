from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required


class DraftListView(LoginRequiredMixin, ListView):
    ''' Blog list view '''
    model = Post
    template_name = "AppBlog/post_draft_list.html"

    def get_queryset(self) -> QuerySet[Any]:
        return Post.objects.filter(
            published_date__isnull=True,
            author=self.request.user
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Draft List"
        context["heading"] = "Draft List"
        return context


class BlogListView(LoginRequiredMixin, ListView):
    ''' Blog list view '''
    model = Post

    def get_queryset(self):
        return Post.objects.filter(
            published_date__isnull=False,
            author=self.request.user
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Post List"
        context["heading"] = "Post List"
        return context


def post_detail(request, pk):
    '''  '''
    post = get_object_or_404(Post, pk=pk)
    comment_list = post.comment_set.all()
    context = {
        "title": "Post Detail",
        "heading": "Post Detail",
        "post": post,
        "comment_list": comment_list,
        "form": CommentForm()
    }
    return render(request, 'AppBlog/post_detail.html', context)


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


@login_required
def post_publish(request, pk):
    '''  '''
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('AppBlog:detail', pk=pk)


@login_required
def comment_add(request, post_pk):
    '''  '''
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            newComm = form.save(commit=False)
            post = get_object_or_404(Post, pk=post_pk)
            newComm.post = post
            newComm.save()
            return redirect("AppBlog:detail", pk=post_pk)
        else:
            form = CommentForm()
    return render(request, 'AppBlog/post_detail.html', {'form': form})


@login_required
def comment_approve(request, post_pk, comm_pk):
    comment = get_object_or_404(Comment, pk=comm_pk)
    comment.approve()
    return redirect('AppBlog:detail', pk=post_pk)


@login_required
def comment_delete(request, post_pk, comm_pk):
    comment = get_object_or_404(Comment, pk=comm_pk)
    result = comment.delete()
    print(result)
    return redirect('AppBlog:detail', pk=post_pk)
