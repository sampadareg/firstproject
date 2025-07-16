from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from post.models import Post
from django.views.generic import CreateView, DetailView, ListView
from post.forms import PostForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


USER = get_user_model()

def list_post(request):
    posts = Post.objects.all()
    return render(
        request, 
        'post/list.html',
        context={
            "posts": posts,
        }
    )

def add_post_view(request):
    context = {
        "author": USER.objects.all()
    }
    return render(request, template_name="post/form.html", context=context)

class CreatePostView(CreateView):
    template_name = "post/form.html"
    form_class = PostForm
    success_url = reverse_lazy("list-post")

class PostDetailView(DetailView):
    model = Post
    template_name = "post/details.html"
    pk_url_kwarg = "id"

def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect(reverse('list-post'))


from django.views.generic import ListView
from .models import Post

class ListPostView(ListView):
    model = Post
    template_name = "post/list.html"
    context_object_name = "posts"

    def get_queryset(self):
        search_value = self.request.GET.get('search', '')
        if search_value:
            return Post.objects.filter(body__icontains=search_value)
        return Post.objects.all()
    # optional, for your template to use
    
    
    