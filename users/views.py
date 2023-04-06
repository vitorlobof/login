from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import User
from hashlib import sha256
import errors as err


def register(request):
    if request.session.get('user_id') is not None:
        return redirect('home')
    
    return render(request, 'register.html', {
        'error_msg': err.msg(request.GET.get('error'))
    })

def validation(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        err.ValidateName(name).valid()
        err.ValidateEmail(email).valid()
        err.ValidatePassword(password).valid()
    except err.RegisterError as e:
        e = err.idx(e)
        return redirect(f'{reverse("register")}?error={e}')

    if User.objects.filter(email=email).first() is not None:
        e = err.idx(err.EmailAlreadyRegisteredError())
        return redirect(f'{reverse("register")}?error={e}')

    password = sha256(password.encode()).hexdigest()
    user = User.objects.create(
        name=name, email=email, password=password)
    
    request.session['user_id'] = user.id
    return redirect('home')

def login(request):
    if request.session.get('user_id') is not None:
        return redirect('home')

    return render(request, 'login.html', {
        'error_msg': err.msg(request.GET.get('error'))
    })

def login_validation(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    password = sha256(password.encode()).hexdigest()

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        e = err.idx(err.EmailNotFoundError())
        return redirect(f'{reverse("login")}?error={e}')

    if user.password != password:
        e = err.idx(err.PasswordIncorrectError())
        return redirect(f'{reverse("login")}?error={e}')
    
    request.session['user_id'] = user.id
    return redirect('home')

def logout(request):
    request.session.flush()
    return redirect('login')
