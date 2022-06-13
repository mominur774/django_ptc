from django.forms import ValidationError
from django.shortcuts import redirect, render
from payment.forms import SubscribedForm
from accounts.models import User
from payment.models import Payment, Withdraw
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def place_order(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.pk)
        payment = Payment.objects.get(user=user)
        form = SubscribedForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            subscribe = form.save(commit=False)
            subscribe.user = request.user
            subscribe.pricing = payment.pricing
            subscribe.is_subscribed = True
            subscribe.save()

            # user.is_subscribed = True
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


@login_required
def withdraw(request):
    if request.method == 'POST':
        withdraw_amount = request.POST.get('withdraw_amount')
        if int(withdraw_amount) > int(request.user.total_earning):
            messages.warning(request, "You don't have enough amount")
        elif int(withdraw_amount) < 1:
            messages.warning(request, "Invalid amount")
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
