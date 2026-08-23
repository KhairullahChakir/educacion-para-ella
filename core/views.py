from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import (
    HeroNews,
    ClassesPageSetting,
    ClassProgram,
    HowItWorksStep,
    Partner,
    AboutStory,
    AboutMilestone,
    FounderCollaborator,
    MethodologyPillar,
    MindfulnessIntro,
    MindfulnessPillar,
    CountryReach,
    VolunteerStat,
    VolunteerRole,
    VolunteerCountry,
    VisionPillar,
    MissionPageSetting,
    CoreValue,
    InvolvementTrack,
    VolunteerJourneyStep,
    FAQItem,
    ContactSetting,
    ContactMessage,
    FooterSetting,
    FooterQuickLink,
    NewsletterSubscriber,
    SocialMediaLink,
    CourseEnrollment,
    StudyMaterial,
)


def home(request):
    """Landing page — public."""
    hero_news_list = HeroNews.objects.filter(is_active=True).order_by('order', '-created_at')
    class_programs = ClassProgram.objects.filter(is_active=True).order_by('order', '-created_at')
    how_it_works_steps = HowItWorksStep.objects.filter(is_active=True).order_by('order', 'step_number')
    partners = Partner.objects.filter(is_active=True).order_by('order', '-created_at')
    enrolled_program_ids = set()
    if request.user.is_authenticated:
        enrolled_program_ids = set(CourseEnrollment.objects.filter(user=request.user, is_active=True).values_list('program_id', flat=True))

    return render(request, 'core/home.html', {
        'hero_news_list': hero_news_list,
        'class_programs': class_programs,
        'how_it_works_steps': how_it_works_steps,
        'partners': partners,
        'enrolled_program_ids': enrolled_program_ids,
    })


@login_required
def dashboard(request):
    """Real Student & Teacher sanctuary dashboard."""
    user_enrollments = CourseEnrollment.objects.filter(user=request.user, is_active=True).select_related('program')
    enrolled_program_ids = set(user_enrollments.values_list('program_id', flat=True))
    available_classes = ClassProgram.objects.filter(is_active=True).exclude(id__in=enrolled_program_ids).order_by('order')
    study_materials = StudyMaterial.objects.filter(is_active=True).order_by('order', '-created_at')
    
    return render(request, 'core/dashboard.html', {
        'user_enrollments': user_enrollments,
        'available_classes': available_classes,
        'study_materials': study_materials,
        'total_active_classes': user_enrollments.count(),
        'enrolled_program_ids': enrolled_program_ids,
    })


@login_required
def enroll_course(request, program_id):
    """1-click enrollment for logged-in students."""
    program = get_object_or_404(ClassProgram, id=program_id, is_active=True)
    enrollment, created = CourseEnrollment.objects.get_or_create(user=request.user, program=program)
    if not enrollment.is_active:
        enrollment.is_active = True
        enrollment.save()
    messages.success(request, f"You are successfully enrolled in {program.title}!")
    # Redirect back to where the student clicked or dashboard
    next_url = request.GET.get('next') or request.META.get('HTTP_REFERER') or '/dashboard/'
    return redirect(next_url)


@login_required
def unenroll_course(request, program_id):
    """Drop/leave an enrolled class."""
    program = get_object_or_404(ClassProgram, id=program_id)
    CourseEnrollment.objects.filter(user=request.user, program=program).delete()
    messages.info(request, f"You have left {program.title}.")
    return redirect('core:dashboard')


def about(request):
    """About Us page — project history, founders, volunteer community."""
    about_story = AboutStory.objects.filter(is_active=True).first()
    milestones = AboutMilestone.objects.filter(is_active=True).order_by('order', 'step_number', 'created_at')
    founders = FounderCollaborator.objects.filter(is_active=True).order_by('order', '-created_at')
    methodology_pillars = MethodologyPillar.objects.filter(is_active=True).order_by('order', '-created_at')
    return render(request, 'core/about.html', {
        'about_story': about_story,
        'milestones': milestones,
        'founders': founders,
        'methodology_pillars': methodology_pillars,
    })


def classes(request):
    """Our Classes page — Language Lab, Skills, and Interactive Class Schedules."""
    classes_setting = ClassesPageSetting.objects.filter(is_active=True).first()
    class_programs = ClassProgram.objects.filter(is_active=True).order_by('order', '-created_at')
    enrolled_program_ids = set()
    if request.user.is_authenticated:
        enrolled_program_ids = set(CourseEnrollment.objects.filter(user=request.user, is_active=True).values_list('program_id', flat=True))

    return render(request, 'core/classes.html', {
        'classes_setting': classes_setting,
        'class_programs': class_programs,
        'enrolled_program_ids': enrolled_program_ids,
    })


def class_detail(request, program_id):
    """Dedicated Course Detail and Registration Page for a specific class."""
    from django.shortcuts import get_object_or_404
    program = get_object_or_404(ClassProgram, id=program_id, is_active=True)
    is_enrolled = False
    if request.user.is_authenticated:
        is_enrolled = CourseEnrollment.objects.filter(user=request.user, program=program, is_active=True).exists()

    related_programs = ClassProgram.objects.filter(is_active=True).exclude(id=program.id).filter(subject_category=program.subject_category).order_by('order')[:3]
    if not related_programs.exists():
        related_programs = ClassProgram.objects.filter(is_active=True).exclude(id=program.id).order_by('order')[:3]

    study_materials = StudyMaterial.objects.filter(is_active=True, subject_category=program.subject_category).order_by('order')[:4]
    if not study_materials.exists():
        study_materials = StudyMaterial.objects.filter(is_active=True).order_by('order')[:4]

    return render(request, 'core/class_detail.html', {
        'program': program,
        'is_enrolled': is_enrolled,
        'related_programs': related_programs,
        'study_materials': study_materials,
    })


def mindfulness(request):
    """Mindfulness & Well-being page."""
    mindfulness_intro = MindfulnessIntro.objects.filter(is_active=True).first()
    mindfulness_pillars = MindfulnessPillar.objects.filter(is_active=True).order_by('order', '-created_at')
    countries = CountryReach.objects.filter(is_active=True).order_by('order', '-created_at')
    return render(request, 'core/mindfulness.html', {
        'mindfulness_intro': mindfulness_intro,
        'mindfulness_pillars': mindfulness_pillars,
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
    mission_setting = MissionPageSetting.objects.filter(is_active=True).first()
    vision_pillars = VisionPillar.objects.filter(is_active=True).order_by('order', '-created_at')
    core_values = CoreValue.objects.filter(is_active=True).order_by('order', 'value_number')
    return render(request, 'core/mission.html', {
        'mission_setting': mission_setting,
        'vision_pillars': vision_pillars,
        'core_values': core_values,
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
