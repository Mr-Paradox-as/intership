import django
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def signupuser(request):
    if request.method == 'GET':
        return render(request,'signupuser.html',{'form':UserCreationForm()})
    else:
        #create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('logupuser')
            except IntegrityError:
                return render(request,'signupuser.html',{'form':UserCreationForm,'error':'That username is already taken please choose another username.'})
        else:
            #tell the user the password are not matching
            return render(request,'signupuser.html',{'form':UserCreationForm ,'error':'Your Password did not match'})

def logupuser(request):
    return render (request,'logup.html')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'signupuser.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user == None:
            return render(request, 'signupuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('logupuser')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
