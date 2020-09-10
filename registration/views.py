from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm
import random
from .models import Profile
from app.models import Order


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.bilance = 0.0
            profile.profit = 0.0
            profile.btc = random.uniform(1, 10)
            profile.deposit = random.uniform(500, 1000)
            profile.user = user
            profile.save()
            return redirect("/")
        else:
            print(profile_form.errors)
    else:
        form = RegisterForm()
        profile_form = ProfileForm()
    return render(request, "registration/register.html", {'form': form, 'profile_form': profile_form})


def account(request):
    profile = Profile.objects.filter(user=request.user.id)[0]
    orders = Order.objects.filter(profile=profile)
    wallet = profile.bilance + profile.deposit
    return render(request, "registration/account.html", {'profile': profile, 'orders': orders, 'wallet': wallet})
