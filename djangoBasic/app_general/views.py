
from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'generals/index.html')

def dashboard(request):
    news = Blog.objects.all().order_by('-pk')
    
    return render(request, 'dashboards/dashboard.html', {
        'news': news
    })

def singUp(request):
    return render(request, 'authentications/signUp.html')

def login(request):
    return render(request, 'authentications/login.html')


# System's functions
def signUpForm(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if password == repassword:
        if User.objects.filter(username=username).exists():
            print("This username is already exist!")
            messages.info(request, 'This username is already exist!')
            return redirect('/signUp')
        elif User.objects.filter(email=email).exists():
            print('This email is already exist!')
            messages.info(request, 'This email is already exist!')
            return redirect('/signUp')
        else:
            user = User.objects.create_user(
                username = username,
                email = email,
                password = password
            )
            user.save()
            return redirect('/login')
    else:
        print('The password do not match!')
        messages.info(request, 'The password do not match!')
        return redirect('/signUp')