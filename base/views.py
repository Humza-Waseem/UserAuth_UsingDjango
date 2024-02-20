from django.shortcuts import render,redirect
from django.contrib import messages  # importing the flash messages 
# Create your views here.
from .models import User
from django.contrib.auth import authenticate,login,logout

from .Forms import UserForm

def UserSignIn(request):
    if request.method == 'POST':
        email  = request.POST.get('email')#  this is the email we enter at the login page,, It has a name attribute of email in the input field
        password = request.POST.get('password')
        try:
            user = User.objects.get(email= email)
        except:
            messages.error(request, 'Email or Password is incorrect')

        user = authenticate(request,email =email,password= password )
        if user is not None:
            login(request,user)
            messages.error(request,"You are logged in")
            return redirect('home')
           
        else:
            messages.error(request,"email or Password is incorrect")

    context = {}
    return render(request,'base/login.html',context)
    
def UserLogout(request):
    logout(request)
    messages.success(request, "You are logged out")
    return redirect('home')


def RegisterUser(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit= False)
            user.save()
            login(request.user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')
    return render(request,'base/RegisterUser.html',{'form':form}) 

def Home(request):
    return render(request, 'base/home.html') 
