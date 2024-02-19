from django.shortcuts import render, redirect
from feedbacks.models import Feedback

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        new_product = Feedback(name=name, email=email, message=message)
        new_product.save()
        return redirect('/')
    else:
        return render(request, 'index.html')