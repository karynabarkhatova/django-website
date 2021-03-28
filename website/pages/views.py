from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Doctor, Contact_Info
from .forms import Contact_Form
from datetime import datetime


def index(request):
    data = Doctor.objects.get(id=1)
    return render(request, 'index.html', {'data': data})


def about(request):
    data = Doctor.objects.get(id=1)
    return render(request, 'about.html', {'data': data})


def contact(request):

    if request.method == 'POST':
        form = Contact_Form(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            response = form.cleaned_data['response']
            data = Contact_Info(first_name=first_name, last_name=last_name, email=email, topic=topic, message=message, response=response)
            data.save()
            return HttpResponseRedirect('/')

    else:
        form = Contact_Form()
        return render(request, 'contact.html', {'form': form})