from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q

from .forms import RegisterForm, TransactionForm
from .models import Transaction, UserAccount


def index(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    return render(request, 'index.html')


def transaction_info(request, transid):
    if not request.user.is_authenticated:
        return redirect('/')

    transaction = Transaction.objects.get(id=transid)

    if not transaction:
        return render(request, 'error.html', {'error': 'Wrong transaction id.'})

    return render(request, 'transaction_info.html', context={'transaction': transaction})

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/')

    return render(request, 'dashboard.html', context={
        'transactions': Transaction.objects.filter(
                Q(from_account=request.user.useraccount) 
                | Q(to_account=request.user.useraccount)
            ).filter(accepted=True).order_by('-date'),
        })

def new_transaction(request):
    if not request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            accountNumber = form.cleaned_data['reciever']
            if len(UserAccount.objects.filter(account_number=accountNumber)) != 1:
                return render(request, 'error.html', {'error': 'Wrong account number.'})

            return render(request, 'confirmation.html', {'transaction': form.cleaned_data})
    else:
        form = TransactionForm()

    return render(request, 'new_transaction.html', {'form': form})

def confirm_transaction(request):
    if not request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        reciever = request.POST['reciever']
        message = request.POST['message']
        amount = int(request.POST['amount'])
        to_user = UserAccount.objects.get(account_number=reciever)

        Transaction.objects.create(
            from_account=request.user.useraccount,
            to_account=to_user,
            amount=amount,
            message=message
        )
    return redirect('dashboard')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})
