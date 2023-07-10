from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import User

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html', {
        'users': User.objects.all()
    })

