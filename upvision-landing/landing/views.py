from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Ваша заявка принята")
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})



