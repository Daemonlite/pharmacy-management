from django import forms
from .models import Drug

class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ['name', 'price', 'description', 'manufacturer', 'supplier_info', 'expiry_date', 'on_sale']
