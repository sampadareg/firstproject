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

class ListPostView(LoginRequiredMixin, ListView):
    template_name = "post/list.html"
    context_object_name = "posts"

    def get_queryset(self):
        search = self.request.GET.get("search", '')
        search_filter = {}

        if search:
            search_filter.update({"body__icontains": search})

        return Post.objects.filter(**search_filter).order_by("id")

    def get_context_data(self, **kwargs):
        from math import ceil

        current_page = int(self.request.GET.get("page", 1))
        all_posts = self.get_queryset()
        total_posts = all_posts.count()
        posts_per_page = 4

        start = (current_page - 1) * posts_per_page
        end = current_page * posts_per_page
        posts = all_posts[start:end]

        total_pages = ceil(total_posts / posts_per_page)

        context = {
            "posts": posts,
            "total_pages": range(total_pages),
            "current_page": current_page - 1,
        }
        return context
