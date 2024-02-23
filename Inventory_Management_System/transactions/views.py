from django.shortcuts import redirect, render, get_object_or_404
from .models import Transaction
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from transactions.models import Transaction
from django.utils import timezone
import mysql.connector

# Create your views here.
@login_required
def transactions(request):
    # transactions = Transaction.objects.all()
    transactions = Transaction.objects.order_by('-datetime')
    is_superuser = request.user.is_superuser
    return render(request, 'transactions.html', {'transactions': transactions, 'is_superuser': is_superuser})

@login_required
def delete_transaction(request, t_id):
    if request.method == 'POST':
        transaction = Transaction.objects.get(t_id=t_id)
        transaction.delete()
        return redirect('/transactions')
    else:
        transaction = get_object_or_404(Transaction, t_id=t_id)
        return render(request, 'transaction_delete.html', {'transaction': transaction})
    