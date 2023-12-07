from django.shortcuts import render
from django.http import HttpResponse
from web.forms import UserForm,LoginForm,URLForm
# Create your views here.
def index(request):
    return HttpResponse("Welcome TO Home Page")


def home(request):
    return render(request,"home.html")

def register_user(request):
   user=UserForm()
   return render(request,"userForm.html",context={"user":user})


def login_user(request):
   user=LoginForm()
   return render(request,"userForm.html",context={"user":user})


def url_user(request):
   url_form=URLForm()
   return render(request,"userurl.html",context={"url":url_form})