from django.shortcuts import render
from inventory.models import Product
from transactions.models import Transaction
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
@login_required
def home(request):
    username = request.user.username
    greeting = greet()
    low_quantity_products = Product.objects.filter(quantity__lt=10).order_by('quantity')
    recent_transactions = Transaction.objects.order_by('-datetime')[:10]
    return render(request, 'home.html', {'recent_transactions': recent_transactions, 'low_quantity_products': low_quantity_products, 'greeting': greeting, 'username': username})

def greet():
    current_time = datetime.datetime.now().time()
    current_hour = current_time.hour

    if current_hour < 12:
        greeting = "Good morning"
    elif current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    return greeting