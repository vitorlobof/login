from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.messages import constants
from .models import User
import users.validations as valid


def register(request):
    if request.user.is_authenticated:
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

    if User.objects.filter(username=name).exists():
        messages.add_message(
            request,
            constants.ERROR,
            'Já existe um usuário com este nome.'
        )
        return redirect('register')

    if User.objects.filter(email=email).exists():
        messages.add_message(
            request, constants.ERROR, 'Email já registrado.')
        return redirect('register')

    user = User.objects.create_user(
        username=name, email=email, password=password)
    
    request.session['user_id'] = user.id
    messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso.')
    return redirect('home')

def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    return render(request, 'login.html')

def login_validation(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = auth.authenticate(request, username=username, password=password)

    if not user:
        messages.add_message(request, constants.ERROR, 'Username ou senha inválidos.')
        return redirect('login')
    

    auth.login(request, user)
    messages.add_message(request, constants.SUCCESS, 'Você está na plataforma.')
    return redirect('home')

def logout(request):
    auth.logout(request)
    messages.add_message(request, constants.WARNING,'Faça login antes de acessar a plataforma.')
    return redirect('login')
