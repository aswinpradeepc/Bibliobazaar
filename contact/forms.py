from django import forms
from .models import Book

class BookRequestForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'email', 'message']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Name of the book'}),
            'author': forms.TextInput(attrs={'placeholder': 'Name of Author'}),
            'publisher': forms.TextInput(attrs={'placeholder': 'Publisher'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Messages, if any'}),
        }
