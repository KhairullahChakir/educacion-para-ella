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


class AuthSetting(models.Model):
    """Dynamic headline, mission badge, and quote displayed on registration and login screens."""
    badge_label = models.CharField(max_length=60, default="EDUCACIÓN PARA ELLA", help_text="Small pill text")
    headline = models.CharField(max_length=200, default="Empowering Afghan Girls & Students Everywhere")
    subheadline = models.TextField(default="Join our supportive community of learners and dedicated international educators. Safe, free, and accessible from home.")
    student_quote = models.TextField(default="“When learning continues at home, hope, knowledge, and future possibilities remain limitless.”")
    quote_author = models.CharField(max_length=100, default="Educación para Ella Community")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Auth Showcase Setting"
        verbose_name_plural = "Auth Showcase Settings"

    def __str__(self):
        return self.headline


class AuthHighlight(models.Model):
    """Key perks and student guarantees displayed in the left panel of registration and login."""
    title = models.CharField(max_length=120, help_text="Perk title (e.g. 100% Free & Open Access)")
    description = models.TextField(help_text="Short explanation")
    icon = models.CharField(max_length=20, default="🎓", help_text="Emoji or icon badge")
    order = models.PositiveIntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Auth Page Perk / Highlight"
        verbose_name_plural = "Auth Page Perks & Highlights"

    def __str__(self):
        return f"{self.icon} {self.title}"


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
