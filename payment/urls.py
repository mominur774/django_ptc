from django.urls import path
from payment import views


urlpatterns = [
    path('place-order/', views.place_order, name="place-order"),
    path('withdraw/', views.withdraw, name="withdraw"),
]
