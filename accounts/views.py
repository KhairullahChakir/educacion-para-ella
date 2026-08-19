from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import AuthSetting, AuthHighlight


def register_view(request):
    """Handle user registration."""
    if request.user.is_authenticated:
        return redirect('core:dashboard')

    auth_setting = AuthSetting.objects.filter(is_active=True).first()
    auth_highlights = AuthHighlight.objects.filter(is_active=True).order_by('order', '-created_at')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to Educación para Ella, {user.username}! Your learning journey begins now.')
            return redirect('core:dashboard')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {
        'form': form,
        'auth_setting': auth_setting,
        'auth_highlights': auth_highlights,
    })


def login_view(request):
    """Handle user login."""
    if request.user.is_authenticated:
        return redirect('core:dashboard')

    auth_setting = AuthSetting.objects.filter(is_active=True).first()
    auth_highlights = AuthHighlight.objects.filter(is_active=True).order_by('order', '-created_at')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'core:dashboard')
                return redirect(next_url)
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {
        'form': form,
        'auth_setting': auth_setting,
        'auth_highlights': auth_highlights,
    })


@login_required
def logout_view(request):
    """Log user out and redirect to home."""
    logout(request)
    messages.info(request, 'You have been safely logged out.')
    return redirect('core:home')
