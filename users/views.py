from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from .models import User
from hashlib import sha256
import users.validations as valid


def register(request):
    if request.session.get('user_id') is not None:
        return redirect('home')
    
    return render(request, 'register.html')

def validation(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        valid.ValidateName(name).valid()
        valid.ValidateEmail(email).valid()
        valid.ValidatePassword(password).valid()
    except valid.RegisterError as e:
        messages.add_message(request, constants.ERROR, e.MSG)
        return redirect('register')

    if User.objects.filter(email=email).first() is not None:
        messages.add_message(
            request, constants.ERROR, 'Email já registrado.')
        return redirect('register')

    password = sha256(password.encode()).hexdigest()
    user = User.objects.create(
        name=name, email=email, password=password)
    
    request.session['user_id'] = user.id
    messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso.')
    return redirect('home')

def login(request):
    if request.session.get('user_id') is not None:
        return redirect('home')

    return render(request, 'login.html')

def login_validation(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    password = sha256(password.encode()).hexdigest()

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        messages.add_message(request, constants.ERROR, 'Email não cadastrado.')
        return redirect('login')

    if user.password != password:
        messages.add_message(request, constants.ERROR, 'Senha incorreta.')
        return redirect('login')
    
    request.session['user_id'] = user.id
    messages.add_message(request, constants.SUCCESS, 'Você está na plataforma.')
    return redirect('home')

def logout(request):
    request.session.flush()
    return redirect('login')
