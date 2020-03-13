from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Client


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Afegeix el teu email")

    class Meta:
        model = Client
        fields = ("email", "username", "password1", "password2")
