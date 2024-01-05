from django.shortcuts import render
from .models import Category,BlogPost
from django.views.generic import ListView,CreateView
from .forms import BlogPostForm


class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog/blog_post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get("category")
        if Category:
            queryset = queryset.filter(category__name=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog/blog_post_create.html"
    success_url = "/blog/"

