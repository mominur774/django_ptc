from django.shortcuts import render
from faq.models import Faq

# Create your views here.


def faqView(request):
    faqs = Faq.objects.all()

    context = {
        'faqs': faqs
    }
    return render(request, 'faq/faqlist.html', context)
