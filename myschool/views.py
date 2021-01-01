from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("helooooo")

def profile(request):
    return HttpResponse("Welcome to my profile")    

def password(request):
    return HttpResponse("You need to register first") 

def register(request):
    return HttpResponse("you must set a PASSWORD to continue")   

def signup(request):
    return render(request,'1.html')

def signup(request):
    return render(request,'form 1.html')   

def project(request):
    return render(request,'PROJECT 3.html')  

def login(request):
    return render(request,'LOGIN PAGE.html') 
