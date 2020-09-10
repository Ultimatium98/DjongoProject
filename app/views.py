from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order
from registration.models import Profile
from django.db.models import Q

def home(request):
    return render(request, 'app/home.html')


def order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            profile = request.user.profile
            new_order = form.save(commit=False)
            new_order.profile = profile
            if new_order.position =='buy':
                orders = Order.objects.filter(~Q(profile=profile) & Q(position='sell') & Q(status='undone') & Q(price__lte=form.instance.price))
                if orders:
                    total_bilance = form.instance.profile.deposit + form.instance.profile.bilance
                    if total_bilance - form.instance.price < 0:
                        msg = "Error! price is higher than your disponibility"
                        return render(request, "app/home.html", {'msg': msg})
                    else:
                        form.instance.status = 'done'
                        orders[0].status = 'done'
                        orders[0].profile.bilance += form.instance.price
                        orders[0].profile.btc -= form.instance.quantity
                        form.instance.profile.bilance -= form.instance.price
                        form.instance.profile.btc += form.instance.quantity
                        form.instance.profile.save()
                        orders[0].save()
                        orders[0].profile.save()
                        form.instance.save()
                        msg = "Transaction done!"
                        return render(request, "app/home.html", {'msg': msg})
                else:
                    if form.instance.quantity <= 0 or form.instance.price <= 0:
                        msg = "Error! Can't accept quantity or price value"
                        return render(request, "app/home.html", {'msg': msg})
                    else:
                        msg = "Wait, a Sell order must be published first"
                        return render(request, "app/home.html", {'msg': msg})
            else:
                if form.instance.quantity <= 0 or form.instance.price <= 0:
                    msg = "Error! Cant' accept quantity or price value"
                    return render(request, "app/home.html", {'msg': msg})
                elif form.instance.profile.btc - form.instance.quantity < 0:
                    msg = "Don't have that much btc"
                    return render(request, "app/home.html", {'msg': msg})
                else:
                    new_order.save()
                    msg = "new order added"
                    return render(request, "app/home.html", {'msg': msg})
    else:
        form = OrderForm()
    return render(request, "app/new_order.html", {'form': form})


def order_list(request):
    orders = Order.objects.filter(status='undone')
    return render(request, 'app/order_list.html', {'orders': orders})


def analytics(request):
    users = Profile.objects.filter()
    for user in users:
        total = user.deposit + user.bilance
        profit = (total - user.deposit)/user.deposit * 100
        user.profit = "{:.2f}".format(profit)
        user.save()
    return render(request, 'app/analytics.html', {'users': users})
# Create your views here.
