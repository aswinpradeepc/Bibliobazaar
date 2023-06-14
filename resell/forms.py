from django import forms
from .models import resell_book

class ResellRequestForm(forms.ModelForm):
    class Meta:
        model = resell_book
        fields = ['title', 'author', 'publisher', 'message', 'cover_image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Name of the book'}),
            'author': forms.TextInput(attrs={'placeholder': 'Name of Author'}),
            'publisher': forms.TextInput(attrs={'placeholder': 'Publisher'}),
            'message': forms.Textarea(attrs={'placeholder': 'Messages, if any'}),
        }
