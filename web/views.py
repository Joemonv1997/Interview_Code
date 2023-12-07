from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from web.forms import UserForm,LoginForm,URLForm
from web.models import SortendURL
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return HttpResponse("Welcome TO Home Page")


def home(request):
    return render(request,"home.html")

def register_user(request):
    if request.method == "POST":
        user = UserForm(request.POST)
        if user.is_valid():
            email = user.cleaned_data['email']
            password = user.cleaned_data['password']
            print(email,password)
            return HttpResponseRedirect("/")
    else:
        user = UserForm()
    return render(request,"userForm.html",context={"user":user})


def login_user(request):
    if request.method == "POST":
        user = LoginForm(request.POST)
        if user.is_valid():
            email = user.cleaned_data['email']
            password = user.cleaned_data['password']
            auth_user = authenticate(request, email=email, password=password)
            print(auth_user)
            if auth_user is not None:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                return render(request,"userForm.html",context={"user":user})
        else:
            render(request,"userForm.html",context={"user":user})
    else:
        user = LoginForm()
    return render(request,"userForm.html",context={"user":user})


def url_user(request):
    if request.method == "POST":
        url_form = URLForm(request.POST)
        if url_form.is_valid():
            url = url_form.cleaned_data['user_url']
            print(url)

            short_url=SortendURL(user_url=url,user=User.objects.get(id=1))

            short_url.save()
            return HttpResponseRedirect("/")
        else:
            return render(request,"userForm.html",context={"url":url_form})
    else:
        url_form=URLForm()
    return render(request,"userurl.html",context={"url":url_form})