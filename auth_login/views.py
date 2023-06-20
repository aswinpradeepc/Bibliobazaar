import logging
from pprint import pprint

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

logger = logging.getLogger('auth')

@ensure_csrf_cookie
def signin(request):
    context1 = {}
    pprint(request.META['QUERY_STRING'])
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, password)
        if not email or not password:
            context1['pswderr'] = "Text fields cannot be empty"
        try:
            user = authenticate(request, username=email, password=password)
            print(f"{user =}")
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next'))
        except User.DoesNotExist:
            context1['pswderr'] = "user does not exist"

    return render(request, template_name='auth_login/login.html', context=context1)


@ensure_csrf_cookie
def signup(request):
    context1 = {}
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        passwrd2 = request.POST.get("password retype")
        username = request.POST.get("username", '')
        print(f"{email = } {password = } {passwrd2} {username = }")
        if not email:
            context1['pswderr'] = 'Email cannot be empty'
            print('Email was empty')
        elif not password or not passwrd2:
            context1['pswderr'] = 'Password cannot be empty'
            print('Password was empty')
        elif not username:
            context1['pswderr'] = 'Username cannot be empty'
            print('Username was empty')
        else:
            if passwrd2 == password:
                try:
                    print("everything is okey creating user ")
                    user = User.objects.create_user(email=email, password=password, username=username,
                                                    first_name=username)
                    print(f"created user {user.username} ")
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    redirect_location = request.GET.get('next', '/') + '?' + request.META['QUERY_STRING']
                    return HttpResponseRedirect(redirect_location)

                except IntegrityError as e:
                    print(e)
                    print('User already exist')
                    context1['pswderr'] = 'User already exists'

            else:
                print('Password Does not match')
                context1['pswderr'] = 'Password Does not match'

    return render(request, template_name="auth_login/signup.html", context=context1)


logger.info


@login_required
def profile_view(request):
    return render(request, template_name='auth_login/profile.html')


@login_required
def log_out(request):
    logout(request)
    url = '/?' + request.META['QUERY_STRING']
    return HttpResponseRedirect(url)
