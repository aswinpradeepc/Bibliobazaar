from django.urls import path, include
from . import views

urlpatterns = [
    path("login/", views.signin, name="login"),
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile_view, name="profile"),
    path("logout/", views.log_out, name="logout"),

]
