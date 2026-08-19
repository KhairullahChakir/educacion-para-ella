from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import HeroNews, ClassProgram, HowItWorksStep


def home(request):
    """Landing page — public."""
    hero_news_list = HeroNews.objects.filter(is_active=True).order_by('order', '-created_at')
    class_programs = ClassProgram.objects.filter(is_active=True).order_by('order', '-created_at')
    how_it_works_steps = HowItWorksStep.objects.filter(is_active=True).order_by('order', 'step_number')
    return render(request, 'core/home.html', {
        'hero_news_list': hero_news_list,
        'class_programs': class_programs,
        'how_it_works_steps': how_it_works_steps,
    })


@login_required
def dashboard(request):
    """Student dashboard — requires authentication."""
    return render(request, 'core/dashboard.html')


def about(request):
    """About Us page — project history, founders, volunteer community."""
    return render(request, 'core/about.html')


def classes(request):
    """Our Classes page — English, Spanish, German, Photography, Programming."""
    class_programs = ClassProgram.objects.filter(is_active=True).order_by('order', '-created_at')
    return render(request, 'core/classes.html', {
        'class_programs': class_programs,
    })


def mindfulness(request):
    """Mindfulness & Well-being page."""
    return render(request, 'core/mindfulness.html')


def volunteers(request):
    """Our Volunteers page."""
    return render(request, 'core/volunteers.html')


def mission(request):
    """Our Mission page — values, vision, empowerment."""
    return render(request, 'core/mission.html')


def get_involved(request):
    """Get Involved page — volunteer, teach, support, partner."""
    return render(request, 'core/get_involved.html')


def contact(request):
    """Contact page — contact info, social media."""
    return render(request, 'core/contact.html')
