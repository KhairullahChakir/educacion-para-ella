from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('classes/', views.classes, name='classes'),
    path('mindfulness/', views.mindfulness, name='mindfulness'),
    path('volunteers/', views.volunteers, name='volunteers'),
    path('mission/', views.mission, name='mission'),
    path('get-involved/', views.get_involved, name='get_involved'),
    path('contact/', views.contact, name='contact'),
    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),
    path('classes/<int:program_id>/', views.class_detail, name='class_detail'),
    path('classes/<int:program_id>/enroll/', views.enroll_course, name='enroll_course'),
    path('classes/<int:program_id>/unenroll/', views.unenroll_course, name='unenroll_course'),
]
