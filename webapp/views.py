from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def home (request):
    if request.user.is_authenticated:
        return  render(request, 'home.html')
    else:
        return redirect('/signin')

def signin(request):
    if request.user.is_authenticated:
        return redirect ('/')
    else:
      if request.method=="POST":
        username=request.POST['username']
        password=request.POST["password"]
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return  redirect('/signin')   
      else:
        return  render(request,"login.html")
      

def signout(request):
   logout(request)
   return redirect('/signin')

def signup(request):
    if request.method =="POST":
      username=request.POST['username']
      password=request.POST['password']
      confpassword=request.POST['confirmpassword']
      phoneno=request.POST['phoneno']
      if password==confpassword:
         user=User.objects.create_user(username=username,password=password)
         user.save()
         login(request,user)
         return redirect('/')
      else:
         return redirect('/signup')
    else:
      return render (request, "signup.html")