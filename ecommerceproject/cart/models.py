from django.db import models
from ecommerceapp.models import Products

# Create your models here.
class Cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='Cart'
        ordering=('date_added',)

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    products=models.ForeignKey(Products,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='CartItem'

    def sub_total(self):
        return self.products.price * self.quantity

    def __str__(self):
        return self.products

