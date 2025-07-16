from django.urls import path
from .views import login_view

urlpatterns = [
    path('', login_view, name='auth-home'),  # this catches /auth/
    path('login/', login_view, name='login'),  # optional, for /auth/login/
]
