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


class Partner(models.Model):
    """Solidarity partners and collaborator organizations."""
    name = models.CharField(max_length=150, help_text="Organization / Partner Name")
    role_description = models.CharField(max_length=150, help_text="Role or support type (e.g. Curriculum & Volunteer Solidarity, Advocacy & Outreach)")
    icon_or_logo = models.CharField(max_length=20, default="🤝", help_text="Icon or flag emoji if no image logo uploaded")
    logo = models.ImageField(upload_to='partner_logos/', blank=True, null=True, help_text="Partner logo (optional)")
    website_url = models.CharField(max_length=255, default="#", help_text="Partner official website or detail URL")
    badge_label = models.CharField(max_length=50, default="Partner", help_text="Small pill badge (e.g. Founding Partner, Strategic Partner, Global Network)")
    order = models.PositiveIntegerField(default=0, help_text="Sort order")
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide this partner")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Partner / Collaborator"
        verbose_name_plural = "Partners & Collaborators"

    def __str__(self):
        return self.name


class AboutStory(models.Model):
    """Dynamic Origin & Purpose section on the About Us page."""
    badge_text = models.CharField(max_length=60, default="Origin & Purpose", help_text="Small category badge")
    headline = models.CharField(max_length=250, default="When classroom doors are closed, we keep learning alive")
    paragraph_1 = models.TextField(help_text="First narrative paragraph explaining the background")
    paragraph_2 = models.TextField(help_text="Second narrative paragraph detailing the initiative response")
    quote_text = models.TextField(help_text="Highlighted inspirational quote banner")
    image = models.ImageField(upload_to='about_images/', blank=True, null=True, help_text="Story illustration or photo")
    is_active = models.BooleanField(default=True, help_text="Active toggle")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "About Page Story"
        verbose_name_plural = "About Page Stories"

    def __str__(self):
        return self.headline


class FounderCollaborator(models.Model):
    """Founders and key leadership collaborators featured on the About Us page."""
    name = models.CharField(max_length=150, help_text="Leader / Founder Name (e.g. Najiah Mohammadi, Chloe, Carol, Ansoh)")
    role_title = models.CharField(max_length=150, help_text="Title / Role (e.g. Founder & Project Lead, Lead Software & AI Engineer, Key Collaborator)")
    organization = models.CharField(max_length=150, default="Educación para Ella", help_text="Affiliated Organization")
    bio = models.TextField(help_text="Detailed profile bio and contribution story")
    location = models.CharField(max_length=150, default="📍 Kabul & Global", help_text="Location / Region")
    image = models.ImageField(upload_to='leader_images/', blank=True, null=True, help_text="Portrait photo or illustrated avatar")
    badge_theme = models.CharField(max_length=30, default="teal", choices=[('teal', 'Teal'), ('amber', 'Amber'), ('purple', 'Purple'), ('blue', 'Blue')], help_text="Visual color accent")
    order = models.PositiveIntegerField(default=0, help_text="Sort order (0 appears first)")
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide this profile")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Founder & Collaborator"
        verbose_name_plural = "Founders & Key Collaborators"

    def __str__(self):
        return f"{self.name} ({self.role_title})"


class MethodologyPillar(models.Model):
    """Holistic Educational Ecosystem pillars on About Us and Mission pages."""
    COLOR_CHOICES = [
        ('teal', 'Teal / Emerald'),
        ('blue', 'Blue / Indigo'),
        ('purple', 'Purple / Violet'),
        ('amber', 'Amber / Warm'),
    ]

    title = models.CharField(max_length=120, help_text="Pillar title (e.g. Languages, Digital & AI Literacy)")
    tag = models.CharField(max_length=100, default="Global Pathways", help_text="Subtitle or focus tag (e.g. Global Communication, Tech Independence)")
    icon = models.CharField(max_length=20, default="🗣️", help_text="Emoji icon (e.g. 🗣️, 💻, 📸, 🧘‍♀️)")
    description = models.TextField(help_text="Core methodology and student impact description")
    skills_list = models.CharField(max_length=255, blank=True, null=True, help_text="Comma-separated skills (e.g. English CEFR A0–C1, Spanish, German)")
    image = models.ImageField(upload_to='methodology_images/', blank=True, null=True, help_text="Header illustration for Option A card")
    link_url = models.CharField(max_length=255, default="/classes/", help_text="Action button link")
    button_text = models.CharField(max_length=60, default="Explore Track →", help_text="Button text")
    badge_color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='teal')
    order = models.PositiveIntegerField(default=0, help_text="Sort order")
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide this pillar")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Methodology Pillar"
        verbose_name_plural = "Methodology Pillars"

    def __str__(self):
        return self.title

    @property
    def color_classes(self):
        if self.badge_color == 'blue':
            return {
                'badge': 'bg-blue-100 text-blue-900 border-blue-200',
                'border_hover': 'hover:border-blue-500',
                'accent': 'text-blue-700',
            }
        elif self.badge_color == 'purple':
            return {
                'badge': 'bg-purple-100 text-purple-900 border-purple-200',
                'border_hover': 'hover:border-purple-500',
                'accent': 'text-purple-700',
            }
        elif self.badge_color == 'amber':
            return {
                'badge': 'bg-amber-100 text-amber-900 border-amber-200',
                'border_hover': 'hover:border-amber-500',
                'accent': 'text-amber-700',
            }
        else:
            return {
                'badge': 'bg-teal-100 text-teal-900 border-teal-200',
                'border_hover': 'hover:border-[#167888]',
                'accent': 'text-[#167888]',
            }
