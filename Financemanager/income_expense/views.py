from django.shortcuts import render, HttpResponse, redirect
from .forms import ExpenseForm, IncomeForm
from .models import Expense, Income
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from .utils import get_plot


# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password==confirm_password:
            user=User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('/')

    else:
        print('laure laglau')
    return render(request, 'register.html')

def user_login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username, password=password)
        if user is not None :
            login(request, user)
            return redirect('dashboard') 
        else:
            return HttpResponse("Wrong credentials")
    else:
        pass
    return render(request, 'login.html')


@login_required
def dashboard(request):
    user=request.user
    expenses = Expense.objects.filter(user=user)
    incomes = Income.objects.filter(user=user)
    expense_date_list=[]
    amount_list=[]
    for expense in expenses:
        expense_date=expense.date.strftime("%Y-%m-%d")
        amount=expense.amount
        expense_date_list.append(expense_date)
        amount_list.append(amount)
    
    chart=get_plot(expense_date_list, amount_list)
    context = {
        'expenses': expenses,
        'incomes': incomes,
        'user': user,
        'chart': chart,
        }
    return render(request, 'dashboard.html', context)

@login_required
def add_expense(request):
    user=request.user
    if request.method == 'POST':
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            expense = expense_form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('dashboard')
    else:
        expense_form = ExpenseForm()

    context = {
        'expense_form': expense_form,
    }
    return render(request, 'dashboard.html', context)

@login_required
def add_income(request):
    user=request.user
    if request.method == 'POST':
        income_form = IncomeForm(request.POST)
        if income_form.is_valid():
            income = income_form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('dashboard')
    else:
        income_form = IncomeForm()

    context = {
        'income_form': income_form,
    }
    return render(request, 'dashboard.html', context)


@login_required
def logout_page(request):
    # user=request.user
    logout(request)
    return redirect('/')
