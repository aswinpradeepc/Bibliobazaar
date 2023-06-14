from django.shortcuts import render
from django.db.models import Count

# Create your views here.
from .models import BookForSale


def shop_grid_view(request):
    books = BookForSale.objects.all()
    count = BookForSale.objects.count()
    offer_books = BookForSale.objects.filter(offer=True)
    used_books = BookForSale.objects.filter(used=True)
    return render(request, 'shop-grid.html',
                  {'books': books, 'offer_books': offer_books, 'count': count, 'used_books': used_books})


def shop_details_view(request):
    # Create a context dictionary with any data you want to pass to the template
    context = {}

    # Render the template with the given context
    return render(request, 'shop-details.html', context)
