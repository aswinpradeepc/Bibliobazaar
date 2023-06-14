from django.db import models
from django.contrib.auth.models import User

class resell_book(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='book_images/resell')
    message = models.TextField()

    def __str__(self):
        return self.title
