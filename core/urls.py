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
]

