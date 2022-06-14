from django.shortcuts import redirect, render
from payment.models import Subscribed, Withdraw
from pricing.models import Pricing
from django.contrib.auth.decorators import login_required
from pricing.models import AdLink
import time
from accounts.models import User, UserReferralCode
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q

# Create your views here.


def index(request):
    all_pricing = Pricing.objects.all()

    context = {
        'all_pricing': all_pricing
    }
    return render(request, 'core/index.html', context)


def about(request):
    return render(request, 'core/about.html')


@login_required
def dashboard(request):
    context = {}
    try:
        user = User.objects.get(pk=request.user.pk)
        subscribed = Subscribed.objects.get(user=user)
        ad_per_day = user.ad_limit
        ads = []
        for i in range(1, ad_per_day+1):
            ads.append(i)
        ad = AdLink.objects.filter(pk__in=ads).order_by('id')
        paginator = Paginator(ad, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'ads_per_day': page_obj,
            'subscribed': subscribed
        }
    except:
        pass
    return render(request, 'core/dashboard.html', context)


@login_required
def decrese_ad(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        user = User.objects.get(pk=request.user.pk)
        subscribed = Subscribed.objects.get(user=user)
        daily_ad_limit = user.ad_limit - 1
        user.ad_limit = daily_ad_limit
        if subscribed.pricing.plan_name == "Level-5":
            user.total_earning += 20
        else:
            user.total_earning += 10
        user.save()
        time.sleep(4)
    # return redirect('/dashboard')
    return redirect(url)


@login_required
def profile(request):
    user = User.objects.get(pk=request.user.pk)
    referral_code = UserReferralCode.objects.get(user=user)
    subscribed = {}
    try:
        subscribed = Subscribed.objects.get(user=user)
    except Exception as e:
        pass

    context = {
        'user': user,
        'referral_code': referral_code,
        'subscribed': subscribed
    }
    return render(request, 'core/profile.html', context)


# Admin panel

@login_required
def reload_site(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            subscribed_user = User.objects.filter(is_subscribed=True)
            subscription = Subscribed.objects.filter(user__in=subscribed_user)
            for sub in subscription:
                for user in subscribed_user:
                    if sub.user == user:
                        user.ad_limit = sub.pricing.ad_limit
                        user.save()
            messages.success(
                request, 'Everything reloaded successfully!')
    else:
        redirect('/accounts/login')
    return render(request, 'admin/reload.html')


@login_required
def activate_deactivate(request):
    if request.user.is_superuser:
        users = User.objects.all().exclude(is_superuser=True)
        if request.method == 'POST':
            user_type = request.POST.get('user_type')
            user_id = request.POST.get('id')
            user = User.objects.get(pk=user_id)
            if user_type == 'activate':
                user.is_active = True
                user.save()
            else:
                user.is_active = False
                user.save()
        context = {
            'users': users
        }
    else:
        return redirect('/accounts/login')
    return render(request, 'admin/activate_deactivate.html', context)


@login_required
def accept_payment(request):
    if request.user.is_superuser:
        payment_requests = Withdraw.objects.filter(paid=False)
        if request.method == 'POST':
            withdraw_id = request.POST.get('id')
            withdraw = Withdraw.objects.get(pk=withdraw_id)
            withdraw.paid = True
            withdraw.save()

        context = {
            'payment_requests': payment_requests
        }
    else:
        return redirect('/accounts/login')
    return render(request, 'admin/accept_payment.html', context)


@login_required
def accept_subscription(request):
    if request.user.is_superuser:
        subscribed_users = Subscribed.objects.filter(
            Q(is_subscribed=True) &
            Q(user__is_subscribed=False)
        )
        if request.method == 'POST':
            user_id = request.POST.get('user_id')
            user = User.objects.get(pk=user_id)
            user.is_subscribed = True
            user.save()
        context = {
            'subscribed_users': subscribed_users
        }
    else:
        return redirect('/accounts/login')
    return render(request, 'admin/accept_subscription.html', context)
