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


class MindfulnessIntro(models.Model):
    """Dynamic Trauma-Informed Learning Intro on the Mindfulness & Well-being page."""
    badge_text = models.CharField(max_length=60, default="Trauma-Informed Learning", help_text="Category pill text")
    headline = models.CharField(max_length=250, default="Healing and learning must go hand in hand")
    paragraph_1 = models.TextField(help_text="First paragraph explaining emotional challenges & context")
    paragraph_2 = models.TextField(help_text="Second paragraph explaining mindfulness circles & facilitator support")
    safety_point_1_title = models.CharField(max_length=100, default="100% Confidential & Safe")
    safety_point_1_desc = models.CharField(max_length=200, default="Camera-optional, anonymous handles respected")
    safety_point_2_title = models.CharField(max_length=100, default="Practical Daily Tools")
    safety_point_2_desc = models.CharField(max_length=200, default="Breathing and somatic exercises usable anytime from home")
    button_text = models.CharField(max_length=60, default="Join Next Safe Circle →", help_text="Action button label")
    button_url = models.CharField(max_length=255, default="/contact/", help_text="Action button destination")
    image = models.ImageField(upload_to='mindfulness_images/', blank=True, null=True, help_text="Mindfulness illustration/artwork")
    is_active = models.BooleanField(default=True, help_text="Active toggle")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Mindfulness Page Intro"
        verbose_name_plural = "Mindfulness Page Intros"

    def __str__(self):
        return self.headline


class CountryReach(models.Model):
    """Four countries reached by the program (Afghanistan, Iran, Pakistan, Iraq)."""
    country_code = models.CharField(max_length=10, default="AF", help_text="ISO Country Code (e.g. AF, IR, PK, IQ)")
    country_name = models.CharField(max_length=100, help_text="Country Name")
    flag_emoji = models.CharField(max_length=20, default="🇦🇫", help_text="Flag Emoji fallback")
    flag_image = models.ImageField(upload_to='flag_images/', blank=True, null=True, help_text="High-res country flag image")
    badge_tag = models.CharField(max_length=80, default="Diaspora Community", help_text="Category tag (e.g. Inside Country, Diaspora Community, Regional Outreach)")
    description = models.TextField(help_text="Description of student support in this country")
    student_impact_label = models.CharField(max_length=100, blank=True, null=True, help_text="e.g. Active Daily Classes, Safe Peer Circles")
    order = models.PositiveIntegerField(default=0, help_text="Sort order")
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide this country")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Country Reach"
        verbose_name_plural = "Country Reaches"

    def __str__(self):
        return f"{self.country_name} ({self.country_code})"


class VolunteerStat(models.Model):
    """Dynamic impact numbers and statistics strip displayed on the Volunteers page."""
    number_value = models.CharField(max_length=50, default="25+", help_text="The stat number / metric (e.g. 25+, 12+, 100+, 4)")
    label = models.CharField(max_length=100, help_text="Stat label (e.g. Active Volunteers, Countries Represented)")
    subtitle = models.CharField(max_length=150, help_text="Stat subtitle explanation (e.g. Teaching & mentoring weekly)")
    color_accent = models.CharField(max_length=30, default="teal", choices=[('teal', 'Teal'), ('amber', 'Amber'), ('blue', 'Blue'), ('purple', 'Purple')], help_text="Number highlight color")
    order = models.PositiveIntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True, help_text="Active toggle")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Volunteer Impact Statistic"
        verbose_name_plural = "Volunteer Impact Statistics"

    def __str__(self):
        return f"{self.number_value} - {self.label}"

    @property
    def text_color_class(self):
        if self.color_accent == 'amber':
            return 'text-amber-600'
        elif self.color_accent == 'blue':
            return 'text-blue-600'
        elif self.color_accent == 'purple':
            return 'text-purple-600'
        else:
            return 'text-[#167888]'


class VolunteerRole(models.Model):
    """Volunteer profile tracks and impact roles displayed on the Volunteers page."""
    COLOR_CHOICES = [
        ('teal', 'Teal / Teaching'),
        ('blue', 'Blue / Tech'),
        ('purple', 'Purple / Well-being'),
        ('amber', 'Amber / Content & Translation'),
    ]

    title = models.CharField(max_length=150, help_text="Role / Track Title (e.g. Language Educators, Software Developers & Tech Mentors)")
    team_badge = models.CharField(max_length=60, default="Teaching Team", help_text="Team category (e.g. Teaching Team, Tech Team, Well-being Team, Content Team)")
    icon = models.CharField(max_length=20, default="👩‍🏫", help_text="Emoji icon (e.g. 👩‍🏫, 💻, 🧘‍♀️, 📖)")
    image = models.ImageField(upload_to='volunteer_role_images/', blank=True, null=True, help_text="Header artwork/illustration for the role card")
    description = models.TextField(help_text="Role overview and contribution summary")
    bullet_1 = models.CharField(max_length=200, help_text="First responsibility/impact point")
    bullet_2 = models.CharField(max_length=200, help_text="Second responsibility/impact point")
    button_text = models.CharField(max_length=60, default="Join this Team →", help_text="Button text")
    button_url = models.CharField(max_length=255, default="/get-involved/", help_text="Target URL")
    color_theme = models.CharField(max_length=30, choices=COLOR_CHOICES, default='teal')
    order = models.PositiveIntegerField(default=0, help_text="Sort order")
    is_active = models.BooleanField(default=True, help_text="Active toggle")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Volunteer Role Track"
        verbose_name_plural = "Volunteer Role Tracks"

    def __str__(self):
        return f"{self.title} ({self.team_badge})"

    @property
    def badge_class(self):
        if self.color_theme == 'blue':
            return "bg-blue-50 text-blue-800 border-blue-200"
        elif self.color_theme == 'purple':
            return "bg-purple-50 text-purple-800 border-purple-200"
        elif self.color_theme == 'amber':
            return "bg-amber-50 text-amber-800 border-amber-200"
        else:
            return "bg-teal-50 text-teal-800 border-teal-200"

    @property
    def bullet_color_class(self):
        if self.color_theme == 'blue':
            return "bg-blue-600"
        elif self.color_theme == 'purple':
            return "bg-purple-600"
        elif self.color_theme == 'amber':
            return "bg-amber-600"
        else:
            return "bg-[#167888]"


class VolunteerCountry(models.Model):
    """Countries and origins from which volunteers connect worldwide."""
    name = models.CharField(max_length=100, help_text="Country Name (e.g. Spain, Germany, United Kingdom, United States, Canada, Greece, Afghan Diaspora)")
    country_code = models.CharField(max_length=10, default="ES", help_text="Country Code (e.g. ES, DE, GB, US, CA, GR, AF)")
    flag_emoji = models.CharField(max_length=20, default="🇪🇸", help_text="Flag Emoji (e.g. 🇪🇸, 🇩🇪, 🇬🇧, 🇺🇸, 🇨🇦, 🇬🇷, 🇦🇫)")
    flag_image = models.ImageField(upload_to='volunteer_flag_images/', blank=True, null=True, help_text="High-res custom flag image")
    description = models.TextField(blank=True, null=True, help_text="Short description of volunteer educators connecting from here")
    tag_label = models.CharField(max_length=60, default="Educators & Mentors", blank=True, null=True, help_text="Category pill badge (e.g. INSIDE COUNTRY, DIASPORA COMMUNITY, SOLIDARITY PARTNER)")
    order = models.PositiveIntegerField(default=0, help_text="Sort order")
    is_active = models.BooleanField(default=True, help_text="Active toggle")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Volunteer Origin Country"
        verbose_name_plural = "Volunteer Origin Countries"

    def __str__(self):
        return f"{self.flag_emoji} {self.name} ({self.country_code})"


class VisionPillar(models.Model):
    """Our Vision for the Future manifesto pillars on the Mission page."""
    COLOR_CHOICES = [
        ('teal', 'Teal'),
        ('blue', 'Blue'),
        ('purple', 'Purple'),
        ('amber', 'Amber'),
    ]

    pillar_number = models.CharField(max_length=20, default="01", help_text="Numeral tag (e.g. 01, 02, 03, 04)")
    title = models.CharField(max_length=150, help_text="Pillar title (e.g. Education Creates Possibilities)")
    description = models.TextField(help_text="Core manifesto message")
    icon = models.CharField(max_length=20, default="🌟", help_text="Emoji icon (e.g. 🌟, 💻, 🤝, 🕊️)")
    image = models.ImageField(upload_to='vision_images/', blank=True, null=True, help_text="Header artwork/illustration for the vision card")
    accent_color = models.CharField(max_length=30, choices=COLOR_CHOICES, default='teal')
    order = models.PositiveIntegerField(default=0, help_text="Sort order")
    is_active = models.BooleanField(default=True, help_text="Active toggle")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Vision Manifesto Pillar"
        verbose_name_plural = "Vision Manifesto Pillars"

    def __str__(self):
        return f"Pillar {self.pillar_number}: {self.title}"

    @property
    def color_classes(self):
        if self.accent_color == 'blue':
            return {
                'badge': 'bg-blue-100 text-blue-900 border-blue-200',
                'border_hover': 'hover:border-blue-400 hover:shadow-blue-50',
                'icon_bg': 'bg-blue-50 text-blue-800 border-blue-100',
                'accent': 'text-blue-700',
            }
        elif self.accent_color == 'purple':
            return {
                'badge': 'bg-purple-100 text-purple-900 border-purple-200',
                'border_hover': 'hover:border-purple-400 hover:shadow-purple-50',
                'icon_bg': 'bg-purple-50 text-purple-800 border-purple-100',
                'accent': 'text-purple-700',
            }
        elif self.accent_color == 'amber':
            return {
                'badge': 'bg-amber-100 text-amber-900 border-amber-200',
                'border_hover': 'hover:border-amber-400 hover:shadow-amber-50',
                'icon_bg': 'bg-amber-50 text-amber-800 border-amber-100',
                'accent': 'text-amber-700',
            }
        else:
            return {
                'badge': 'bg-teal-100 text-teal-900 border-teal-200',
                'border_hover': 'hover:border-[#167888] hover:shadow-teal-50',
                'icon_bg': 'bg-teal-50 text-[#167888] border-teal-100',
                'accent': 'text-[#167888]',
            }


class InvolvementTrack(models.Model):
    """Specialized volunteer and partnership opportunities on the Get Involved page."""
    COLOR_CHOICES = [
        ('teal', 'Teal / Teaching'),
        ('purple', 'Purple / Mindfulness'),
        ('blue', 'Blue / Tech & Translation'),
        ('amber', 'Amber / Institutional Partner'),
    ]

    track_number = models.CharField(max_length=20, default="01", help_text="Track number (e.g. 01, 02, 03, 04)")
    title = models.CharField(max_length=150, help_text="Track Title (e.g. Volunteer Language Teacher, Mindfulness Facilitator)")
    badge_label = models.CharField(max_length=60, default="TEACHING TRACK", help_text="Badge label (e.g. TEACHING TRACK, WELL-BEING, TECH & CODE, PARTNERSHIP)")
    icon = models.CharField(max_length=20, default="👩‍🏫", help_text="Emoji icon (e.g. 👩‍🏫, 🧘‍♀️, 💻, 🤝)")
    image = models.ImageField(upload_to='involvement_images/', blank=True, null=True, help_text="Header illustration for the opportunity card")
    description = models.TextField(help_text="Track overview and role expectations")
    commitment_info = models.CharField(max_length=150, default="2 to 4 hours per week", help_text="Weekly time commitment")
    skills_or_platform = models.CharField(max_length=200, default="Zoom / Google Meet with curriculum provided", help_text="Platform or background required")
    button_text = models.CharField(max_length=60, default="Apply Now →", help_text="Button text")
    button_url = models.CharField(max_length=255, default="/accounts/register/", help_text="Target URL")
    color_theme = models.CharField(max_length=30, choices=COLOR_CHOICES, default='teal')
    order = models.PositiveIntegerField(default=0, help_text="Sort order")
    is_active = models.BooleanField(default=True, help_text="Active toggle")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Involvement Opportunity Track"
        verbose_name_plural = "Involvement Opportunity Tracks"

    def __str__(self):
        return f"Track {self.track_number}: {self.title}"

    @property
    def style_classes(self):
        if self.color_theme == 'purple':
            return {
                'border_hover': 'hover:border-purple-500 hover:shadow-purple-100',
                'badge': 'bg-purple-50 text-purple-800 border-purple-200',
                'icon_bg': 'bg-purple-600 text-white',
                'bullet_dot': 'bg-purple-600',
                'button': 'bg-purple-700 hover:bg-purple-800 text-white shadow-purple-200',
            }
        elif self.color_theme == 'blue':
            return {
                'border_hover': 'hover:border-blue-500 hover:shadow-blue-100',
                'badge': 'bg-blue-50 text-blue-800 border-blue-200',
                'icon_bg': 'bg-blue-600 text-white',
                'bullet_dot': 'bg-blue-600',
                'button': 'bg-blue-700 hover:bg-blue-800 text-white shadow-blue-200',
            }
        elif self.color_theme == 'amber':
            return {
                'border_hover': 'hover:border-amber-500 hover:shadow-amber-100',
                'badge': 'bg-amber-50 text-amber-800 border-amber-200',
                'icon_bg': 'bg-amber-600 text-white',
                'bullet_dot': 'bg-amber-600',
                'button': 'bg-amber-500 hover:bg-amber-600 text-gray-900 shadow-amber-200',
            }
        else:
            return {
                'border_hover': 'hover:border-[#167888] hover:shadow-teal-100',
                'badge': 'bg-teal-50 text-teal-800 border-teal-200',
                'icon_bg': 'bg-[#167888] text-white',
                'bullet_dot': 'bg-[#167888]',
                'button': 'bg-[#167888] hover:bg-teal-800 text-white shadow-teal-200',
            }


class VolunteerJourneyStep(models.Model):
    """Step-by-step onboarding journey on the Get Involved page."""
    step_number = models.PositiveIntegerField(default=1, help_text="Stage number (1, 2, 3, 4)")
    title = models.CharField(max_length=150, help_text="Step Title (e.g. 1. Apply Online, 2. Intro Chat)")
    description = models.TextField(help_text="Detailed description of what happens at this stage")
    icon_emoji = models.CharField(max_length=20, default="📝", blank=True, null=True, help_text="Optional emoji icon")
    order = models.PositiveIntegerField(default=0, help_text="Sort order")
    is_active = models.BooleanField(default=True, help_text="Active toggle")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'step_number']
        verbose_name = "Volunteer Journey Step"
        verbose_name_plural = "Volunteer Journey Steps"

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"


class FAQItem(models.Model):
    """Frequently asked questions on Get Involved and information pages."""
    CATEGORY_CHOICES = [
        ('volunteer', 'Volunteer & Teaching'),
        ('students', 'Students & Classes'),
        ('safety', 'Safety & Privacy'),
        ('general', 'General Questions'),
    ]

    question = models.CharField(max_length=255, help_text="The question title")
    answer = models.TextField(help_text="The detailed answer text")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='volunteer')
    icon = models.CharField(max_length=20, default="💡", blank=True, null=True, help_text="Emoji icon badge")
    order = models.PositiveIntegerField(default=0, help_text="Sort order (0 appears first)")
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide this FAQ")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "FAQ Item"
        verbose_name_plural = "FAQ Items"

    def __str__(self):
        return self.question
