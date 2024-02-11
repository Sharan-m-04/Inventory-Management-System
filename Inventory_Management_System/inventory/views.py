from django.shortcuts import redirect, render
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.

@login_required
def inventory(request):
    all_products = Product.objects.all()
    is_superuser = request.user.is_superuser

    return render(request, 'inventory.html', {
        'products':all_products,
        'is_superuser': is_superuser,
    })


@login_required
def search_products(request):
    search_query = request.GET.get('search_query', '')
    matched_products = Product.objects.filter(prod_name__icontains=search_query)
    matched_products_data = [{'prod_name': product.prod_name, 'price': product.price, 'quantity': product.quantity, 'prod_id': product.prod_id} for product in matched_products]
    return JsonResponse({'products': matched_products_data})

@login_required
def add_product(request):
    if request.method == 'POST':
        prod_id = request.POST.get('prod_id')
        prod_name = request.POST.get('prod_name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        new_product = Product(prod_id=prod_id,prod_name=prod_name, price=price, quantity=quantity)
        new_product.save()
        
        messages.success(request, 'Product added successfully.')
        return redirect('/inventory')
    else:
        return render(request, 'add.html')

@login_required
def edit_product(request, product_id):
    if request.method == 'GET':
        product = Product.objects.get(prod_id=product_id)
        return render(request, 'edit.html', {'product': product})
    elif request.method == 'POST':
        product = Product.objects.get(prod_id=product_id)
        product.prod_name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.quantity = request.POST.get('quantity')
        product.save()
        messages.success(request, 'Product updated successfully.')
        return redirect('/inventory')

@login_required
def delete_product(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(prod_id=product_id)
        product.delete()
        messages.success(request, f'Product "{product.prod_name}" deleted successfully.')
        return redirect('/inventory')
    else:
        product = Product.objects.get(prod_id=product_id)
        return render(request, 'delete.html', {'product': product})
    