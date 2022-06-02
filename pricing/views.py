from django.shortcuts import redirect, render, get_object_or_404
from pricing.models import Pricing
# from payment.forms import PaymentMethodForm
from payment.models import Payment
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def pricing_plan(request):
    if not request.user.is_subscribed:
        all_pricing = Pricing.objects.all()

        context = {
            'all_pricing': all_pricing
        }
        return render(request, 'pricing/plan.html', context)
    else:
        return redirect('/dashboard')


@login_required
def get_plan(request, slug):
    pricing = get_object_or_404(Pricing, slug=slug)
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        if request.method == 'POST':
            fullname = request.POST.get('fullname')
            phone_number = request.POST.get('phone_number')
            payment_method = request.POST.get('payment_method')

            Payment.objects.create(
                user=request.user,
                pricing=pricing,
                fullname=fullname,
                phone_number=phone_number,
                payment_method=payment_method
            )
            messages.success(request, "Your payment information is recorded")
            return redirect('/place-order')

    context = {
        'pricing': pricing,
    }
    return render(request, 'pricing/get_plan.html', context)
