from django.urls import path
from .views import (BlogListView, BlogCreateView, BlogDetailView,
                    BlogUpdateView, BlogDeleteView, DraftListView, post_publish)

app_name = "AppBlog"

urlpatterns = [
    path('list/', BlogListView.as_view(), name="list"),
    path('draft/list', DraftListView.as_view(), name="draft_list"),
    path('detail/<int:pk>', BlogDetailView.as_view(), name="detail"),
    path('new/', BlogCreateView.as_view(), name="create"),
    path('edit/<int:pk>', BlogUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name="delete"),
    path('publish/<int:pk>', view=post_publish, name="publish"),
]
