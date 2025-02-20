from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('orders', views.orders, name='orders'),
    path('create', views.create, name='create'),
    path('edit', views.edit, name='edit'),
    path('delete', views.delete, name='delete'),
    path('report', views.report, name='report'),
    path('search', views.search, name='search')
    ]