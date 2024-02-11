from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.

def signup(request):
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(username=name, email=email, password=password)
        return redirect('/dashboard')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']

        isUser = auth.authenticate(username=name, password=password)

        if isUser is not None:
            auth.login(request, isUser)
            print("Logged In")
        else:
            print("Authentication Failed")
        
        return redirect('/dashboard')
    else:
        return render(request, 'login.html')
    
def logout_view(request):
    logout(request)
    print("Logged Out")
    return redirect('/')