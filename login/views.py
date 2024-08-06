from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('transacao_list')
    
    next_url = request.GET.get('next')
    if next_url:
        messages.info(request, "Por favor, faça login para acessar esta página.")
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next_url or 'transacao_list')
        else:
            messages.error(request, "Usuário ou senha incorretos.")
    
    return render(request, 'login/login.html')

def erro_view(request):
    return render(request, 'login/erro.html')
