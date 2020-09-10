from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('new-order/', views.order, name='order'),
    path('order-list', views.order_list, name='order_list'),
    path('analytics', views.analytics, name='analytics'),
]