from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Transaction


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username',  'email', 'password1', 'password2',)


class dotdict(dict):
    __getattr__ = dict.get


def TransactionQueryForm(transactions):
    return list(map(lambda row: dotdict({
            'from_account': {
                'account_number': row[1],
                'user': {
                        'username': row[0]
                    }
                },
            'to_account': {
                'account_number': row[3],
                'user': {
                        'username': row[2] 
                    }
                },
            'amount': row[4],
            'date': row[5],
            'message': row[6],
            'id': row[7]
        }), transactions))


class TransactionForm(forms.Form):
    reciever = forms.CharField(label='Reciever')
    message = forms.CharField(label='Message')
    amount = forms.IntegerField(label='Amount', min_value=0)
