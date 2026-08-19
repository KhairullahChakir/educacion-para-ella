from django.db import models


class HeroNews(models.Model):
    """News and announcements displayed dynamically in the hero banner."""
    badge_text = models.CharField(max_length=50, default="LATEST NEWS", help_text="Small pill badge text (e.g. LATEST NEWS, ANNOUNCEMENT)")
    title = models.CharField(max_length=200, help_text="Main headline text")
    subtitle = models.TextField(help_text="Subtitle or description text")
    button_text = models.CharField(max_length=50, default="START FOR FREE", help_text="CTA button text")
    button_url = models.CharField(max_length=255, default="/register/", help_text="Link URL for button")
    image = models.ImageField(upload_to='news_images/', blank=True, null=True, help_text="News image. If left blank, default image is used.")
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide this news item from the home page banner")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Hero News Item"
        verbose_name_plural = "Hero News Items"

    def __str__(self):
        return f"{self.badge_text}: {self.title}"


class ClassProgram(models.Model):
    """Dynamic class and course programs displayed in the Home page slider and Classes page."""
    STATUS_OPEN = 'open'
    STATUS_CLOSED = 'closed'
    STATUS_NOT_REQUIRED = 'not_required'
    STATUS_CUSTOM = 'custom'

    REGISTRATION_STATUS_CHOICES = [
        (STATUS_OPEN, 'Registration Open'),
        (STATUS_CLOSED, 'Registration Closed / Full'),
        (STATUS_NOT_REQUIRED, 'No Reg Required (Open Access)'),
        (STATUS_CUSTOM, 'Custom Status Text'),
    ]

    title = models.CharField(max_length=150, help_text="Class/Subject name (e.g. Spanish Language, Web Development)")
    icon_or_flag = models.CharField(max_length=20, default="🇬🇧", help_text="Emoji icon or flag (e.g. 🇬🇧, 🇪🇸, 🇩🇪, 💻, 📸, 🧘‍♀️, 🖥️)")
    badge_text = models.CharField(max_length=60, default="CEFR A0–A2", help_text="Level/Tag badge (e.g. CEFR A0–C1, JavaScript & Web, Visual Arts)")
    track_type = models.CharField(max_length=60, default="All Levels", help_text="Track category (e.g. All Levels, Beginner Track, Digital Track, Well-being)")
    description = models.TextField(help_text="Short overview of what students will learn")
    schedule_time = models.CharField(max_length=120, default="Mon & Wed · 4:00 PM", help_text="Days & time / schedule info (e.g. Mon & Wed · 4:00 PM, Weekly Saturdays, Flexible Hours)")
    status = models.CharField(max_length=30, choices=REGISTRATION_STATUS_CHOICES, default=STATUS_OPEN, help_text="Registration availability status")
    custom_status_text = models.CharField(max_length=50, blank=True, null=True, help_text="Custom status label if 'Custom Status Text' selected above")
    image = models.ImageField(upload_to='class_images/', blank=True, null=True, help_text="Course cover photo (optional, nice default used if blank)")
    button_text = models.CharField(max_length=60, default="Explore levels →", help_text="Action link text")
    button_url = models.CharField(max_length=255, default="/classes/", help_text="Target URL")
    order = models.PositiveIntegerField(default=0, help_text="Sort order in the slider (0 appears first)")
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide this class from the slider")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Class Program"
        verbose_name_plural = "Class Programs"

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"

    @property
    def display_status(self):
        if self.status == self.STATUS_CUSTOM and self.custom_status_text:
            return self.custom_status_text
        return self.get_status_display()

    @property
    def status_badge_classes(self):
        if self.status == self.STATUS_OPEN:
            return "bg-emerald-100 text-emerald-800 border-emerald-200"
        elif self.status == self.STATUS_CLOSED:
            return "bg-red-100 text-red-800 border-red-200"
        elif self.status == self.STATUS_NOT_REQUIRED:
            return "bg-teal-100 text-teal-800 border-teal-200"
        else:
            return "bg-amber-100 text-amber-800 border-amber-200"


class HowItWorksStep(models.Model):
    """Dynamic student onboarding stages displayed on the Home page."""
    step_number = models.PositiveIntegerField(default=1, help_text="Stage number (e.g. 1, 2, 3)")
    title = models.CharField(max_length=150, help_text="Stage title (e.g. Sign Up for Free, Choose Your Subject)")
    description = models.TextField(help_text="Detailed description of what happens at this stage")
    image = models.ImageField(upload_to='step_images/', blank=True, null=True, help_text="Illustration/Photo representing this step")
    button_text = models.CharField(max_length=60, blank=True, null=True, help_text="Optional link/button text")
    button_url = models.CharField(max_length=255, blank=True, null=True, help_text="Optional link target")
    order = models.PositiveIntegerField(default=0, help_text="Sort order")
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide this step")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'step_number']
        verbose_name = "How It Works Step"
        verbose_name_plural = "How It Works Steps"

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"
