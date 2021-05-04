from django.shortcuts import render,redirect,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from files.models import data

# Create your views here.

def login(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.info(request,'*Invalid Credentials')
            return render(request, 'login.html')
    
    else:
        return render(request, 'login.html')


def register(request):

    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'*Username taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name = firstname,last_name = lastname, password = password , username = username)
                user.save()
                messages.info(request,'User created')
                return redirect('login')
                
        else:
            messages.info(request,'Passwords dont match')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def home(request):

    if request.user.is_authenticated:
        all_data = data.objects.all()
        return render(request, 'home.html',{'all_data':all_data})
    
    return redirect('login')
    
    

def logout(request):
    auth.logout(request)
    return redirect('/')