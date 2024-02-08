from django.shortcuts import render

# Create your views here.
def transactions(request):
    return render(request, 'transactions.html')