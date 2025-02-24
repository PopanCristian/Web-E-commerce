from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category, Product


# Create your views here.
@login_required(login_url='/login/')
def orderNow_view(request):
    categories = Category.objects.all()  
    return render(request, 'order.html', {'categories': categories})

def category_products(request, category_name):
    category = get_object_or_404(Category, name_category = category_name)
    products = Product.objects.filter(product_category =category) 

    return render(request, 'category_product.html', {'category': category, 'products': products})