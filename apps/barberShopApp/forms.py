from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Client


class RegistrationForm(UserCreationForm):

    #email = forms.EmailField(max_length=60, required= True)

    class Meta:
        model = Client
        fields = ("username",
                  'email',
                  'first_name',
                  'last_name',
                  "phone",
                  'sexe',
                  "password1",
                  "password2")
    # def save(self, commit=True):
    #     user = super(RegistrationForm, self).save(commit=False)
    #     user.first_name = cleaned_data['first_name']