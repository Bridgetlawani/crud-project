from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView 
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import Post


# Create your views here.
class PostListView(ListView):
    model = Post
    templates_name = "post_list.html"


class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all") 
    templates_name = "post_form.html"

class PostDetailView(DetailView):
    model = Post
    templates_name = "post_detail.html"
      

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all") 
    templates_name = "post_form.html"

class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    templates_name = "post_confirm_delete.html"    