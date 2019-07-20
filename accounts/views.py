from django.shortcuts import render

# Create your views here.

def signup(req):
    return render(req , 'accounts/signup.html')

def login(req):
    return render(req , 'accounts/signin.html')