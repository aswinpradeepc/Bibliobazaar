from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=200)
    city = forms.CharField(max_length=100)
    postcode = forms.CharField(max_length=10)
    phone = forms.CharField(max_length=15)
    notes = forms.CharField(widget=forms.Textarea, required=False)
