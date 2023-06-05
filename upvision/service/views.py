from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def service(request):
    return render(request, 'service.html')


def documentation(request):
    return render(request, 'documentation.html')

def contacts(request):
    return render(request, 'contacts.html')