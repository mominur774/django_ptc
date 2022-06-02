from django.urls import path
from faq import views


urlpatterns = [
    path('faq/', views.faqView, name="faq"),
]
