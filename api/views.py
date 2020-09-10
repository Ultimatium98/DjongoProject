from django.shortcuts import render
from app.models import Order


def order_list(request):
    orders = Order.objects.filter(status='undone')
    return render(request, 'app/order_list.html', {'orders': orders})

# Create your views here.
