# search/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('search_books', views.search_books, name='search_books'),
]
