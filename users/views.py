from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import Profile
from .forms import ProfileForm

# Create your views here.
@login_required
def home(request):
    print(request.user)
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'users/home.html', {'profile':profile})

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
    form = UserCreationForm
    context = {'form' : form}
    return render(request, 'users/registration.html', context)

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form  = AuthenticationForm


def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def update_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {'form' : form}

    return render(request, 'users/profile-update-form.html', context)
