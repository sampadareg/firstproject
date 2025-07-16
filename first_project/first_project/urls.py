from django.contrib import admin
from django.urls import path, include
from post.views import list_post, add_post_view, CreatePostView, PostDetailView, delete_post, ListPostView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('post/', list_post, name="list-post"),
    path("add-post/", add_post_view, name="add-post"),
    path("create-post/", CreatePostView.as_view(), name="create-post"),
    path("post-detail/<int:id>/", PostDetailView.as_view(), name="post-detail-url"),
    path("post-delete/<int:id>/", delete_post, name="delete-post"),
    path('posts/', ListPostView.as_view(), name='post-list'),
    
    path('super-admin/login/', auth_views.LoginView.as_view(), name='login'),
    
    path("auth/", include('authentication.urls')), 
    path('logout/', auth_views.LogoutView.as_view(next_page='auth-home'), name='logout'),# Make sure authentication.urls has patterns!
]
