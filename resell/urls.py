from django.urls import path
from resell.views import *

urlpatterns = [
    path('resell', resell_view),
]