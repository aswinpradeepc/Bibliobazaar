from django.contrib.auth.models import User
from django.db import models


class BookForSale(models.Model):
    image = models.ImageField(upload_to='book_images')
    title = models.CharField(max_length=255)
    department = models.CharField(max_length=100)
    offer = models.BooleanField(default=False)
    used = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    author = models.CharField(max_length=100, default='No author provided')
    description = models.TextField(default='No description provided')
    preview_1 = models.ImageField(upload_to='book_images', null=True, blank=True)
    preview_2 = models.ImageField(upload_to='book_images', null=True, blank=True)
    preview_3 = models.ImageField(upload_to='book_images', null=True, blank=True)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(BookForSale, on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    notes = models.TextField(blank=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Order {self.pk} - {self.user.username}"
