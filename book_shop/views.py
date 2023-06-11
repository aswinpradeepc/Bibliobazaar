from django.shortcuts import render

# Create your views here.
from .models import BookForSale

def shop_grid_view(request):
    books = BookForSale.objects.all()
    offer_books = BookForSale.objects.filter(offer=True)
    return render(request, 'shop-grid.html', {'books': books, 'offer_books': offer_books})
