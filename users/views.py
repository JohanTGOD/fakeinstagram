from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from users.models import Profile
from django.db.utils import IntegrityError


def my_profile(request):
    return render(request, 'users/myprofile.html')


def login_views(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("correct")
            login(request, user)
            return redirect('show_all_post_url')
        else:
            print("incorrect")
            return render(request, "users/login.html", {'error': 'invalid username or password'})

    return render(request, 'users/login.html')


def sing_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html',
                          {'error': 'Username already exits or the password does not achieve with the paramaters'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return render(request, 'users/login.html')
    return render(request, 'users/signup.html')
