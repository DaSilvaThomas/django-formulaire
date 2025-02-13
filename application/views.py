from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.user.is_authenticated:  # Vérifie si l'utilisateur est déjà connecté
        return redirect('home')  # Redirige vers la page d'accueil

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'application/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige vers la page de connexion après la déconnexion


@login_required(login_url='login')  # Redirige vers /login si non connecté
def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Les utilisateurs non connecté sont redirigés vers la page login
    return render(request, 'application/home.html')


def registration_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connexion automatique après l'inscription
            return redirect('home')  # Redirige vers la page d'accueil après inscription
    else:
        form = RegistrationForm()

    return render(request, 'application/registration.html', {'form': form})
 
