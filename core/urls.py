from django.urls import path
from core import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about, name="about"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('profile/', views.profile, name="profile"),
    path('decrese-ad/', views.decrese_ad, name="decrese-ad"),

    # admin panel
    path('reload/', views.reload_site, name="reload"),
    path('accept-user/', views.accept_user, name="accept-user"),
    path('activate-deactivate/', views.activate_deactivate,
         name="activate-deactivate"),
    path('accept-payment/', views.accept_payment, name="accept-payment"),
]
