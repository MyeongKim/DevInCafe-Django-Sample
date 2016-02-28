from django.shortcuts import render, redirect
from django.contrib.auth.views import login as auth_login
from test2.forms import CustomUserCreationForm


def login(request):
    return auth_login(request)


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'registration/signup.html', context)