from django.shortcuts import redirect, render
from payment.forms import SubscribedForm
from accounts.models import User
from payment.models import Payment, Withdraw
from django.contrib import messages

# Create your views here.


def place_order(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.pk)
        payment = Payment.objects.get(user=user)
        form = SubscribedForm(request.POST)
        if form.is_valid():
            subscribe = form.save(commit=False)
            subscribe.user = request.user
            subscribe.pricing = payment.pricing
            subscribe.save()

            user.is_subscribed = True
            user.ad_limit = subscribe.pricing.ad_limit
            user.save()
            messages.success(
                request, 'Your payment is successull, We will activate your sucscription soon.')
            return redirect('/dashboard')
    form = SubscribedForm()

    context = {
        'form': form
    }
    return render(request, 'payment/place_order.html', context)


def withdraw(request):
    if request.method == 'POST':
        withdraw_amount = request.POST.get('withdraw_amount')
        if int(withdraw_amount) > int(request.user.total_earning):
            print("Don't have enough amount")
        elif int(withdraw_amount) < 1:
            print("Invalid amount")
        else:
            user = User.objects.get(pk=request.user.pk)
            Withdraw.objects.create(
                user=user,
                amount=withdraw_amount
            )
            user.total_earning -= int(withdraw_amount)
            user.save()
            print("Withdraw successfull")
            return redirect('/dashboard')
    return render(request, 'payment/withdraw.html')
