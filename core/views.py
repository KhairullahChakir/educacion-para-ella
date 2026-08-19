from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import (
    HeroNews,
    ClassesPageSetting,
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
    FAQItem,
    ContactSetting,
    ContactMessage,
    FooterSetting,
    FooterQuickLink,
    NewsletterSubscriber,
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
    """Our Classes page — Language Lab, Skills, and Interactive Class Schedules."""
    classes_setting = ClassesPageSetting.objects.filter(is_active=True).first()
    class_programs = ClassProgram.objects.filter(is_active=True).order_by('order', '-created_at')
    return render(request, 'core/classes.html', {
        'classes_setting': classes_setting,
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
    faqs = FAQItem.objects.filter(is_active=True).order_by('order', '-created_at')
    return render(request, 'core/get_involved.html', {
        'involvement_tracks': involvement_tracks,
        'volunteer_journey_steps': volunteer_journey_steps,
        'faqs': faqs,
    })


def contact(request):
    """Contact page — contact info, WhatsApp, direct messaging."""
    contact_info = ContactSetting.objects.filter(is_active=True).first()

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        topic = request.POST.get('topic', 'General Inquiry').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                topic=topic,
                message=message,
            )
            messages.success(request, "Thank you! Your message has been safely received. Our team will get back to you shortly.")
            return redirect('core:contact')
        else:
            messages.error(request, "Please fill in all required fields before submitting.")

    return render(request, 'core/contact.html', {
        'contact_info': contact_info,
    })


def subscribe_newsletter(request):
    """Handle footer newsletter subscriptions."""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            NewsletterSubscriber.objects.create(name=name)
            messages.success(request, f"Thank you {name}! You have been subscribed to our updates.")
        else:
            messages.error(request, "Please enter your name to subscribe.")
            
    next_url = request.POST.get('next', request.META.get('HTTP_REFERER', '/'))
    return redirect(next_url)
