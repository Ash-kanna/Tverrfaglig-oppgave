from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("members/", views.member_list, name="members"),
    path("activities/", views.activity_list, name="activities"),
    path("activities/new/", views.activity_create, name="activity_create"),
    path("activities/delete/<int:activity_id>/", views.activity_delete, name="activity_delete"),
    path("activities/join/<int:activity_id>/", views.activity_join, name="activity_join"),
    path("activities/leave/<int:activity_id>/", views.activity_leave, name="activity_leave"),

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
    path("members/delete/<int:user_id>/", views.member_delete, name="member_delete"),
]