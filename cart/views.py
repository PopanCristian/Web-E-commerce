from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart

#view cart
def cart_view(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
    else:
        cart_items = []

    total_price = sum(item.quantity * item.product.product_price for item in cart_items)

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


#add a product in cart
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(product=product, user=request.user)

    if created: #if it's first time is 1, if we orderd multiple same product we add 1
        cart_item.quantity = 1  
    else:
        cart_item.quantity += 1 

    cart_item.save()
    return redirect('cart:cart_view')

def cart_total_quantity(request): # for the context processor to show everywhere
    if request.user.is_authenticated:
        total_quantity = sum(item.quantity for item in Cart.objects.filter(user=request.user))
    else:
        total_quantity = 0

    return {'total_quantity': total_quantity}