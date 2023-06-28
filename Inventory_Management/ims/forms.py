from django import forms
from . models import Brands, Product, Purchase, Manage

# class Category(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['name',]
#
#         widgets = {
#             'name': forms.TextInput(attrs={'class':'form-control'}),
#        }

class BrandsForm(forms.ModelForm):
    class Meta:
        model = Brands
        fields = ['category', 'brand_name']

        widgets = {
            'category': forms.Select(attrs={'class':'form-control'}),
            'brand_name': forms.TextInput(attrs={'class':'form-control'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'brand_name', 'product_name', 'product_model',
                  'description','quantity', 'product_price','product_tax', 'name']

        widgets = {
            'category': forms.Select(attrs={'class':'form-control'}),
            'brand_name': forms.Select(attrs={'class':'form-control'}),
            'product_name':forms.TextInput(attrs={'class':'form-control'}),
            'product_model': forms.TextInput(attrs={'class':'form-control'}),
            'quantity': forms.TextInput(attrs={'class':'form-control'}),
            'product_price': forms.TextInput(attrs={'class':'form-control'}),
            'product_tax': forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.Select(attrs={'class':'form-control'}),
        }
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['product_name', 'quantity', 'name']

        widgets = {
            'product_name': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.Select(attrs={'class': 'form-control'}),
        }

class ManageForm(forms.ModelForm):
    class Meta:
        model = Manage
        fields = ['product_name', 'total_item','name']

        widgets = {
            'product_name': forms.Select(attrs={'class':'form-control'}),
            'total_item': forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.Select(attrs={'class':'form-control'}),
        }