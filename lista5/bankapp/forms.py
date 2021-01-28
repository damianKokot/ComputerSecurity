from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Transaction


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username',  'email', 'password1', 'password2',)


class TransactionForm(forms.Form):
    reciever = forms.CharField(label='Reciever')
    message = forms.CharField(label='Message')
    amount = forms.IntegerField(label='Amount', min_value=0)
