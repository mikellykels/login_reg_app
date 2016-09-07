from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    return render(request, 'login_reg_app/index.html')

def login(request):
    if request.method == "POST":
        result = User.userMgr.login(
            email       =   request.POST['email'],
            password    =   request.POST['password']
        )
        if result[0]:
            request.session['user_id'] = result[1].id
            request.session['user_firstname'] = result[1].first_name
            return redirect(reverse('success'))
        else:
            for error in result[1]:
                messages.add_message(request, messages.INFO, result[1][error])
            return redirect(reverse('index'))
    else:
        return redirect(reverse('index'))

def register(request):
    if request.method == "POST":
        result = User.userMgr.register(
            first_name  =   request.POST['first_name'],
            last_name   =   request.POST['last_name'],
            email       =   request.POST['email'],
            password    =   request.POST['password'],
            confirm_pw  =   request.POST['confirm_pw']
        )
        if result[0]:
            request.session['user_id'] = result[1].id
            request.session['user_firstname'] = result[1].first_name
            return redirect(reverse('success'))
        else:
            for error in result[1]:
                messages.add_message(request, messages.INFO, result[1][error])
            return redirect(reverse('index'))
    else:
        return redirect(reverse('index'))

def logout(request):
    request.session.pop('user_id')
    request.session.pop('user_firstname')
    return redirect(reverse('index'))
