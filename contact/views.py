from django.shortcuts import redirect, render
from contact.forms import ContactForm

# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact')
    form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'core/contact.html', context)
