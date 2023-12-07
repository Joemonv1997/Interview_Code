from django.urls import path
from web import views
urlpatterns = [
    path("", views.index,name="index"),
    path("home", views.home,name="home"),
    path("register", views.register_user,name="sign-up"),
    path("login", views.login_user,name="login"),
]
