from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index , name = 'index'),
    path('admin/', admin.site.urls),
    path('accounts/register', views.register, name = 'register'),
    path('accounts/login/', views.user_login, name = 'user_login'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('add_expense', views.add_expense, name = 'add_expense'),
    path('add_income', views.add_income, name = 'add_income'),
    path('logout', views.logout_page, name = 'logout_page'),
    path('add_payment', views.add_payment, name = 'add_payment'),
]
