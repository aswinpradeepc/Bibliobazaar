from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    # Create a context dictionary with any data you want to pass to the template
    context = {
    }

    # Render the template with the given context
    return render(request, 'index.html', context)


def signup_view(request):
    # Create a context dictionary with any data you want to pass to the template
    context = {

    }

    # Render the template with the given context
    return render(request, 'auth_login/signup.html', context)


def login_view(request):
    # Create a context dictionary with any data you want to pass to the template
    context = {

    }

    # Render the template with the given context
    return render(request, 'auth_login/login.html', context)




def shopping_cart_view(request):
    # Create a context dictionary with any data you want to pass to the template
    context = {

    }

    # Render the template with the given context
    return render(request, 'shopping-cart.html', context)


def checkout_view(request):
    # Create a context dictionary with any data you want to pass to the template
    context = {

    }

    # Render the template with the given context
    return render(request, 'checkout.html', context)

