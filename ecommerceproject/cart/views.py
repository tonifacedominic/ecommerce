from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from ecommerceapp.models import Products
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def add_cart(request,product_id):

# Getting Product and cart for particular product
    product=Products.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
                                cart_id=_cart_id(request)
                                )
        cart.save()

# Adding Item to cart
    try:
        cart_item=CartItem.objects.get(products=product,cart=cart)
        if cart_item.quantity < cart_item.products.stock:
         cart_item.quantity +=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
                                            products=product,
                                            quantity=1,
                                            cart=cart
                                         )
        cart_item.save()
    return redirect('cart:cart_detail')

def cart_detail(request):
    total=0
    counter=0
    cart_items=None
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items=CartItem.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total+=(cart_item.products.price * cart_item.quantity)
            counter += cart_item.quantity

    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))

def remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    products=get_object_or_404(Products,id=product_id)
    cart_item=CartItem.objects.get(cart=cart,products=products)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart:cart_detail')

def deletion(request, product_id):
   cart=Cart.objects.get(cart_id=_cart_id(request))
   product=get_object_or_404(Products, id=product_id)
   cart_item=CartItem.objects.get(cart=cart, products=product)

   cart_item.delete()


   return redirect('cart:cart_detail')






