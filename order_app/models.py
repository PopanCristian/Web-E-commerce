import datetime
from django.db import models

# Categories of Products
class Category( models.Model):
    name_cateogiry = models.CharField(max_length = 30)

    def __str__(self):
        return self.name_category

class Customer( models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 30)
    password = models.CharField(max_length = 75)

    def __str__(self):
        return f"User: {self.first_name} {self.last_name} with phone number: {self.phone}"

class Product( models.Model):
    product_name = models.CharField(max_length = 50)
    product_price = models.DecimalField(default=0, decimal_places = 2, max_digits = 5)
    product_category = models.ForeignKey(Category, on_delete = models.CASCADE, default="None")
    product_description = models.CharField(max_length = 300, default='', null=True)
    product_image = models.ImageField(upload_to='images_products')

    def __str__(self):
        return f"produsul cu numele {self.product_name}"

class Order( models.Model):
    order_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    adress =models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=10, blank = False)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.order_product}"