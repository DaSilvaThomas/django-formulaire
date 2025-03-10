from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Modification de la classe CharField pour empêcher certains caractères spéciaux dans les noms d'utilisateurs
class SafeCharField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(
            validators=[
                RegexValidator(
                    regex=r"^[a-zA-Z0-9_.-]+$",
                    message="Caractères spéciaux interdits.",
                    code="invalid_username",
                )
            ],
            *args,
            **kwargs
        )


# Formulaire de connexion
class LoginForm(AuthenticationForm):
    username = SafeCharField(  # Utilisation de notre classe personnalisé
        label="Nom d’utilisateur",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d’utilisateur'})
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'})
    )


# Formulaire d'inscription
class RegistrationForm(UserCreationForm):
    username = SafeCharField(  # Utilisation de notre classe personnalisé
        label="Nom d’utilisateur",
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d’utilisateur'})
    )
    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'})
    )
    password2 = forms.CharField(
        label="Confirmation du mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmez le mot de passe'})
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]