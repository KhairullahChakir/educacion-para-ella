from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """Profile extending default User model with role and preferences."""

    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )

    LANGUAGE_CHOICES = (
        ('en', 'English'),
        ('fa', 'دری (Dari)'),
        ('ps', 'پښتو (Pashto)'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student', help_text="User role: Student or Teacher")
    preferred_language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='en')
    bio = models.TextField(blank=True, help_text="Optional short biography or introduction")

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"

    @property
    def is_teacher(self):
        return self.role == 'teacher'

    @property
    def is_student(self):
        return self.role == 'student'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """Automatically create or save UserProfile when User instance is created/updated."""
    if created:
        UserProfile.objects.create(user=instance)
    else:
        if hasattr(instance, 'profile'):
            instance.profile.save()
        else:
            UserProfile.objects.create(user=instance)
