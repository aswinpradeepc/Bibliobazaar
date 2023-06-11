from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.title
