from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login  
from django.views.generic import CreateView
from authentication.forms import ProfileForm

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        return redirect('post-list')  # 👈 redirects to list.html via this URL name
    return render(request, 'auth/login_form.html', {'form': form})
class CreateProfileView(CreateView):
    form_class = ProfileForm
    template_name = "profile_form.html"
