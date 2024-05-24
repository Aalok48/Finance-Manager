from django import forms 
from .models import Income, Expense, ToPay

class ExpenseForm(forms.ModelForm):
    category = forms.ChoiceField(
        choices = [
            ('Food','Food'),
            ('Transportion','Transportation'),
            ('Utilities','Utilities'),
            ('Clothes','Clothes'),
            ('Subscription','Subscription'),
            ('Miscellanious','Miscellanous'),
        ]
    )
    class Meta:
        model = Expense
        fields = ['amount', 'category', 'description']

class IncomeForm(forms.ModelForm):
    source = forms.ChoiceField(
        choices = [
            ('Salary', 'Salary'),
            ('Interest income', 'Interest income'),
            ('Rent', 'Rent'),
            ('Inheritance','Inheritance'),
            ('Gift', 'Gift'),
            ('Bheek', 'Bheek'),
            ('Others', 'Others')
        ]
    )
    class Meta:
        model = Income
        fields = ['amount', 'source', 'description']

class TopayForm(forms.ModelForm):
    class Meta:
        model = ToPay
        fields = ['amount', 'date_to_pay', 'reason']