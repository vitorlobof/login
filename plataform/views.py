from django.shortcuts import render, redirect

def home(request):
    user_id = request.session.get('user_id')
    if user_id is None:
        return redirect('login')
    
    return render(request, 'home.html')

