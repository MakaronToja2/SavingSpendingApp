from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return render(request, 'accounts/success.html')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'accounts/login.html', {'error': 'Invalid login'})
    else:
        return render(request, 'accounts/login.html')
