from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('users-registration')
        else:
            messages.error(request, 'Account creation failed')
            return redirect('users-registration')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})