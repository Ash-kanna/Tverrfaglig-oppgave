from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),

    # authentication
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="myapp/login.html"),
        name="login",
    ),
    # logout uses a confirmation page; POST to actually log out
    path(
        "logout/",
        auth_views.LogoutView.as_view(
            template_name="myapp/logout_confirm.html",
            next_page="home",
        ),
        name="logout",
    ),
]