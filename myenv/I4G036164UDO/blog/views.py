from audioop import reverse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name: "blog/post_list.html"

class PostCreateView(CreateView):
    model = Post
    field = "__all__"
    success_url: reverse_lazy('blog:all')
    template_name: "blog/post_form.html"

class PostDetailView(DetailView):
    model = Post
    template_name: "blog/post_detail.html"

class PostUpdateView(UpdateView):
    model = Post
    field = "__all__"
    success_url: reverse_lazy('blog:all')
    template_name: "blog/post_form.html"

class PostDeleteView(DeleteView):
    model = Post
    field = "__all__"
    success_url: reverse_lazy('blog:all')
    template_name: "blog/post_confirm_delete.html"