from django.urls import path
from pricing import views


urlpatterns = [
    path('pricing/', views.pricing_plan, name="pricing"),
    path('get_plan/<str:slug>/', views.get_plan, name="get_plan"),
]
