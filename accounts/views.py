from django.shortcuts import redirect, render
from accounts.forms import SignUpForm, LoginForm, UserPasswordChangeForm, ResetForm, ResetConfirmForm
from django.contrib.auth import authenticate, login, logout
import random
from accounts.models import User, UserReferralCode
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        referral_code = request.POST.get('referral_code')

        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            if UserReferralCode.objects.filter(referral_code=referral_code).exists():
                referral_user = UserReferralCode.objects.get(
                    referral_code=referral_code)
                us = User.objects.get(pk=referral_user.user.pk)
                us.total_earning += 100
                us.save()
            user.otp = str(random.randint(1000, 9999))
            user.is_active = False
            user.save()
            messages.success(
                request, 'Account created successfully!')
            return redirect(f'/accounts/confirm-email/?phone={user.phone_number}')
    else:
        signup_form = SignUpForm()
    context = {
        'signup_form': signup_form,
    }
    return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=phone_number, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                if user.is_superuser:
                    return redirect('/reload')
                if user.is_subscribed:
                    return redirect('/dashboard')
                else:
                    return redirect('/pricing')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logoutView(request):
    logout(request)
    messages.success(request, "Successfully loged out")
    return redirect('/accounts/login')


@method_decorator(login_required, name='dispatch')
class UserPasswordChange(PasswordChangeView):
    template_name = 'accounts/changepass.html'
    form_class = UserPasswordChangeForm


class UserPasswordResetView(PasswordResetView):
    template_name = 'accounts/resetpass.html'
    form_class = ResetForm


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/resetconfirm.html'
    form_class = ResetConfirmForm


def confirm_mail_view(request):
    phone = request.GET.get('phone')
    if request.method == 'POST':
        user = User.objects.get(phone_number=phone)
        otp = request.POST.get('otp')
        if user.otp == otp:
            user.is_active = True
            user.save()
            messages.success(
                request, 'Your account activated please login to continue.')
            return redirect('/accounts/login')
        else:
            messages.error(
                request, "OTP doesn't match. Please enter correct OTP.")
    return render(request, 'accounts/confirmemail.html')
