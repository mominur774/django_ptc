from django.urls import path
from accounts import views
from django.contrib.auth.views import PasswordChangeDoneView, PasswordResetDoneView, PasswordResetCompleteView

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logoutView, name="logout"),
    path('password-change/', views.UserPasswordChange.as_view(),
         name="password-change"),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name='accounts/changedone.html'),
         name="password_change_done"),

    path('password_reset/', views.UserPasswordResetView.as_view(),
         name="password_reset"),
    path('password_reset_done/',
         PasswordResetDoneView.as_view(template_name="accounts/resetdone.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='accounts/resetcomplete.html'),
         name="password_reset_complete")
]
