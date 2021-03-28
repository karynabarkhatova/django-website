from django.shortcuts import render
from .models import Doctor


def index(request):
    data = Doctor.objects.get(id=1)
    return render(request, 'index.html', {'data': data})


def about(request):
    data = Doctor.objects.get(id=1)
    return render(request, 'about.html', {'data': data})


def contact(request):
    return render(request, 'contact.html')