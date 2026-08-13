from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import HeroNews


def home(request):
    """Landing page — public."""
    hero_news_list = HeroNews.objects.filter(is_active=True).order_by('order', '-created_at')
    return render(request, 'core/home.html', {
        'hero_news_list': hero_news_list,
    })


@login_required
def dashboard(request):
    """Student dashboard — requires authentication."""
    return render(request, 'core/dashboard.html')
