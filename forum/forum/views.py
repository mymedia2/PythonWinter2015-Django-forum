from django.shortcuts import render

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=username):
            return render(request, 'register.html',
                    {'errors': 'This username is already taken'})

        user = User.objects.create_user(username=username, password=password)

        if user:
            user = auth.authenticate(username=username, password=password)
            auth.login(request,user)
            return HttpResponseRedirect(reverse('main.views.forum'))

        return render(request, str(user))
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect(reverse('main.views.forum'))
        else:
            return render(request, 'login.html', {'errors': 'Wrong login or username'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main.views.forum'))

def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('main.views.forum'))
    else:
        return HttpResponseRedirect(reverse(login))
