from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        passwordrepeat = request.POST['passwordrepeat']

        if password == passwordrepeat:
            if User.objects.filter(email==email).exists():
                messages.info(request, 'Email already used')

    return render(request, 'register.html')