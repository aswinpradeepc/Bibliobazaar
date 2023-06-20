from django.shortcuts import render, get_object_or_404
from django.http import Http404


# Create your views here.
from .models import BookForSale


def shop_grid_view(request):
    books = BookForSale.objects.all()
    count = BookForSale.objects.count()
    offer_books = BookForSale.objects.filter(offer=True)
    used_books = BookForSale.objects.filter(used=True)
    return render(request, 'shop-grid.html',
                  {'books': books, 'offer_books': offer_books, 'count': count, 'used_books': used_books})

def shop_details_view(request, id):
    try:
        obj = get_object_or_404(BookForSale, id=id)
        context = {'obj': obj}
        return render(request, 'shop-details.html', context)
    except BookForSale.DoesNotExist:
        raise Http404("BookForSale does not exist")
