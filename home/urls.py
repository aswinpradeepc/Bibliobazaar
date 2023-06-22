from django.contrib import admin
from django.urls import path
from home.views import *
from contact.views import contact_view

urlpatterns = [
    path('', home_view),
    path('signup', signup_view),
    path('login', login_view),

]
