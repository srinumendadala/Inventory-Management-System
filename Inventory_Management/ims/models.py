from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    mobile = models.CharField(max_length=13, null=False, blank=False)
    address = models.TextField()
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Brands(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=False)
    brand_name = models.CharField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.brand_name

class Supplier(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    mobile = models.CharField(max_length=100, null=False, blank=False)
    address = models.TextField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=False)
    brand_name = models.ForeignKey(Brands, on_delete=models.CASCADE, default=True, null=False)
    product_name = models.CharField(max_length=100, null=False, blank=False)
    product_model = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    quantity = models.IntegerField()
    product_price = models.DecimalField(max_digits=20, decimal_places=2)
    product_tax = models.IntegerField()
    name = models.ForeignKey(Supplier, on_delete=models.CASCADE, default=True, null=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name

class Purchase(models.Model):
    product_name = models.ForeignKey(Product,on_delete=models.CASCADE, default=True,null=False)
    quantity = models.IntegerField()
    name = models.ForeignKey(Supplier,on_delete=models.CASCADE, default=True,null=False)


class Manage(models.Model):
    product_name = models.ForeignKey(Product,on_delete=models.CASCADE, default=True,null=False)
    total_item = models.IntegerField()
    name = models.ForeignKey(Customer,on_delete=models.CASCADE, default=True,null=False)

