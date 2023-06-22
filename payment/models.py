from django.db import models


# Create your models here.
# transaction model for Razorpay payment gateway

class Transaction(models.Model):
    razorpay_payment_id = models.CharField(max_length=255)
    razorpay_order_id = models.CharField(max_length=255)
    razorpay_signature = models.CharField(max_length=255)
    order = models.ForeignKey('book_shop.Order', on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.CharField(max_length=255, choices=(
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ), default='pending')

    def __str__(self):
        return self.razorpay_order_id




