from django.urls import path
from book_shop.views import *

urlpatterns = [
    path('shop-grid', shop_grid_view),
    #Dynamic url for individual book
    path('shop-details/<int:id>', shop_details_view,name='shop-details'),
]