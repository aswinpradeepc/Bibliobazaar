from django.db import models


class BookForSale(models.Model):
    image = models.ImageField(upload_to='book_images')
    title = models.CharField(max_length=255)
    department = models.CharField(max_length=100)
    offer = models.BooleanField(default=False)
    used = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(default='No description provided')
    preview_1 = models.ImageField(upload_to='book_images', null=True, blank=True)
    preview_2 = models.ImageField(upload_to='book_images', null=True, blank=True)
    preview_3 = models.ImageField(upload_to='book_images', null=True, blank=True)

    def __str__(self):
        return self.title
