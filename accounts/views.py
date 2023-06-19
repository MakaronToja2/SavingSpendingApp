from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import UserProfile

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return render(request, 'accounts/logout.html')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'accounts/login.html', {'error': 'Invalid login'})
    else:
        return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'accounts/logout.html')

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            return redirect('login_view')  # redirect to the login page after registration
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})