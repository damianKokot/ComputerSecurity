from django.urls import path, include, re_path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('register', views.register, name='register'),
  path('dashboard', views.dashboard, name='dashboard'),
  path('transaction/new', views.new_transaction, name='new_transaction'),
  path('transaction/new/confirm', views.confirm_transaction, name='confirm_transaction'),
  re_path(r'transaction/(?P<transid>\d+)$', views.transaction_info, name='transaction_info'),
]
