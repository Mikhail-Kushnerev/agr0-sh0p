from re import A
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User
from .forms import UserCreationForm, LoginForm
# Create your views here.

def user_registr(request):
    template = 'user/registration.html'
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(
            'user:login'
        )
    return render(
        request,
        template,
        {'form': form}
    )

def user_login(request):
    template = 'user/login.html'
    # form = AuthenticationForm(
    #     request.method=='POST' or None, 
    #     data=request.POST
    # )
    # if form.is_valid():
    #     return redirect(
    #         'sales_backend:main_page'
    #     )
    # return render(
    #     request,
    #     template,
    #     {'form': form}
    # )     
    #    
    
    form = LoginForm(request.POST or None)
    if form.is_valid():
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(
                    'sales_backend:main_page'
                )
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    return render(request, 'user/login.html', {'form': form})
