from django.urls import path
from AppBlog import views

app_name = "AppBlog"

urlpatterns = [
    path('list/', views.BlogListView.as_view(), name="list"),
    path('draft/list', views.DraftListView.as_view(), name="draft_list"),
    path('detail/<int:pk>', views.post_detail, name="detail"),
    path('new/', views.BlogCreateView.as_view(), name="create"),
    path('edit/<int:pk>', views.BlogUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', views.BlogDeleteView.as_view(), name="delete"),
    path('<int:pk>/publish/', view=views.post_publish, name="publish"),
    path('<int:post_pk>/comment/add', view=views.comment_add, name="comment_add"),
    path('<int:post_pk>/comment/<int:comm_pk>/approve',
         view=views.comment_approve, name="comment_approve"),
    path('<int:post_pk>/comment/<int:comm_pk>/delete',
         view=views.comment_delete, name="comment_delete"),
]
