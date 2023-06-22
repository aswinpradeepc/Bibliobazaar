from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import time
from .forms import *
# Create your views here.
from .models import *


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


@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(BookForSale, id=book_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item = CartItem.objects.create(cart=cart, book=book)

    if request.method == 'POST':
        if cart_item:
            return redirect('/shopping-cart')
    else:
        return redirect('/shop-details' + '/' + str(book_id))


@login_required
def shopping_cart_view(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = None

    cart_items = cart.cartitem_set.all() if cart else []

    total_price = sum(item.book.price for item in cart_items) if cart_items else 0

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'item_count': len(cart_items),
        'total_price': total_price,
    }
    return render(request, 'shopping-cart.html', context)


def department_view(request, dept):
    if dept == 'used':
        obj = BookForSale.objects.filter(used=True)
    else:
        obj = BookForSale.objects.filter(department=dept)

    count = len(obj)

    context = {'obj': obj, 'dept': dept, 'count': count}

    # Render the template with the given context
    return render(request, 'departments.html', context)


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    messages.success(request, 'Item removed from cart successfully.')
    return redirect('/shopping-cart')


@login_required
def checkout_view(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = None

    cart_items = cart.cartitem_set.all() if cart else []
    total_price = sum(item.book.price for item in cart_items) if cart_items else 0

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order(
                user=request.user,
                name=form.cleaned_data['name'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                postcode=form.cleaned_data['postcode'],
                phone=form.cleaned_data['phone'],
                notes=form.cleaned_data['notes'],
                total_price=total_price
            )
            order.save()
            # You can perform any additional logic here, such as creating invoices, processing payments, etc.
            # Redirect to a success page or do other necessary actions.

    else:
        form = OrderForm()

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'form': form
    }

    return render(request, 'checkout.html', context)
