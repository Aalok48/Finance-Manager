from django import template

register = template.Library()

@register.filter
def calculate_total_expenses(expenses):
    total_expenses = sum(expense.amount for expense in expenses)
    return total_expenses

@register.filter
def calculate_total_incomes(incomes):
    total_incomes = sum(income.amount for income in incomes)
    return total_incomes
