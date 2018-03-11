from django.urls import path
from django.views.generic import ListView, DetailView
from blog.models import Post


urlpatterns = [
    path('', ListView.as_view(queryset=Post.objects.all()
                              .order_by("-date")[:10],
                              template_name="blog/blog.html")),
]
