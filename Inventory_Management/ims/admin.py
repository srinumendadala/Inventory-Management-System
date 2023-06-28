from django.contrib import admin
from . models import Customer, Category, Brands, Supplier, Product, Purchase, Manage
# Register your models here.

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Brands)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Manage)
# username= "raju" & password= 'welcome@123'