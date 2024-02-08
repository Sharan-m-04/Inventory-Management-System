from django.shortcuts import render

# Create your views here.
def inventory(request):
    return render(request, 'inventory.html')