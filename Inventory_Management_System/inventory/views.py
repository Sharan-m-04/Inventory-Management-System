from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def inventory(request):
    all_products = Product.objects.all()

    return render(request, 'inventory.html', {
        'products':all_products,
    })