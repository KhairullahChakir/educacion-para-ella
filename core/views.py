from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import (
    HeroNews,
    ClassProgram,
    HowItWorksStep,
    Partner,
    AboutStory,
    FounderCollaborator,
    MethodologyPillar,
    MindfulnessIntro,
    CountryReach,
    VolunteerStat,
    VolunteerRole,
    VolunteerCountry,
    VisionPillar,
    InvolvementTrack,
    VolunteerJourneyStep,
)


def home(request):
    """Landing page — public."""
    hero_news_list = HeroNews.objects.filter(is_active=True).order_by('order', '-created_at')
    class_programs = ClassProgram.objects.filter(is_active=True).order_by('order', '-created_at')
    how_it_works_steps = HowItWorksStep.objects.filter(is_active=True).order_by('order', 'step_number')
    partners = Partner.objects.filter(is_active=True).order_by('order', '-created_at')
    return render(request, 'core/home.html', {
        'hero_news_list': hero_news_list,
        'class_programs': class_programs,
        'how_it_works_steps': how_it_works_steps,
        'partners': partners,
    })


@login_required
def dashboard(request):
    """Student dashboard — requires authentication."""
    return render(request, 'core/dashboard.html')


def about(request):
    """About Us page — project history, founders, volunteer community."""
    about_story = AboutStory.objects.filter(is_active=True).first()
    founders = FounderCollaborator.objects.filter(is_active=True).order_by('order', '-created_at')
    methodology_pillars = MethodologyPillar.objects.filter(is_active=True).order_by('order', '-created_at')
    return render(request, 'core/about.html', {
        'about_story': about_story,
        'founders': founders,
        'methodology_pillars': methodology_pillars,
    })


def classes(request):
    """Our Classes page — English, Spanish, German, Photography, Programming."""
    class_programs = ClassProgram.objects.filter(is_active=True).order_by('order', '-created_at')
    return render(request, 'core/classes.html', {
        'class_programs': class_programs,
    })


def mindfulness(request):
    """Mindfulness & Well-being page."""
    mindfulness_intro = MindfulnessIntro.objects.filter(is_active=True).first()
    countries = CountryReach.objects.filter(is_active=True).order_by('order', '-created_at')
    return render(request, 'core/mindfulness.html', {
        'mindfulness_intro': mindfulness_intro,
        'countries': countries,
    })


def volunteers(request):
    """Our Volunteers page."""
    volunteer_stats = VolunteerStat.objects.filter(is_active=True).order_by('order', '-created_at')
    volunteer_roles = VolunteerRole.objects.filter(is_active=True).order_by('order', '-created_at')
    volunteer_countries = VolunteerCountry.objects.filter(is_active=True).order_by('order', '-created_at')
    return render(request, 'core/volunteers.html', {
        'volunteer_stats': volunteer_stats,
        'volunteer_roles': volunteer_roles,
        'volunteer_countries': volunteer_countries,
    })


def mission(request):
    """Our Mission page — values, vision, empowerment."""
    vision_pillars = VisionPillar.objects.filter(is_active=True).order_by('order', '-created_at')
    return render(request, 'core/mission.html', {
        'vision_pillars': vision_pillars,
    })


def get_involved(request):
    """Get Involved page — volunteer, teach, support, partner."""
    involvement_tracks = InvolvementTrack.objects.filter(is_active=True).order_by('order', '-created_at')
    volunteer_journey_steps = VolunteerJourneyStep.objects.filter(is_active=True).order_by('order', 'step_number')
    return render(request, 'core/get_involved.html', {
        'involvement_tracks': involvement_tracks,
        'volunteer_journey_steps': volunteer_journey_steps,
    })


def contact(request):
    """Contact page — contact info, social media."""
    return render(request, 'core/contact.html')
