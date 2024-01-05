from django.urls import path
from .views import BlogPostListView,BlogPostCreateView

urlpatterns = [
    path("",BlogPostListView.as_view(),name="blog_post_list"),
    path("create/",BlogPostCreateView.as_view(),name="blog_post_create")
]