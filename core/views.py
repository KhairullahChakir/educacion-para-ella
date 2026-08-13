from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    """Landing page — public."""
    return render(request, 'core/home.html')


@login_required
def dashboard(request):
    """Student dashboard — requires authentication."""
    return render(request, 'core/dashboard.html')
