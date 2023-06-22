from django.urls import path
from book_shop.views import *

urlpatterns = [
    path('shop-grid', shop_grid_view),
    # Dynamic url for individual book
    path('shop-details/<int:id>', shop_details_view, name='shop-details'),
    path('shopping-cart', shopping_cart_view),
    path('checkout', checkout_view),
    path('departments/<str:dept>', department_view, name='departments'),
    path('add-to-cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
]
