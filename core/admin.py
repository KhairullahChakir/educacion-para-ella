from django.contrib import admin
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
    FAQItem,
)


@admin.register(HeroNews)
class HeroNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'badge_text', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'subtitle', 'badge_text')


@admin.register(ClassProgram)
class ClassProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'badge_text', 'schedule_time', 'status', 'order', 'is_active', 'created_at')
    list_filter = ('status', 'is_active', 'created_at')
    list_editable = ('status', 'order', 'is_active')
    search_fields = ('title', 'description', 'badge_text', 'schedule_time')
    fieldsets = (
        ('General Information', {
            'fields': ('title', 'icon_or_flag', 'badge_text', 'track_type', 'description', 'image')
        }),
        ('Schedule & Registration', {
            'fields': ('schedule_time', 'status', 'custom_status_text', 'button_text', 'button_url')
        }),
        ('Visibility & Ordering', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(HowItWorksStep)
class HowItWorksStepAdmin(admin.ModelAdmin):
    list_display = ('step_number', 'title', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'description')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'badge_label', 'role_description', 'website_url', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    list_editable = ('order', 'is_active')
    search_fields = ('name', 'role_description', 'badge_label')


@admin.register(AboutStory)
class AboutStoryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'badge_text', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    list_editable = ('is_active',)
    search_fields = ('headline', 'paragraph_1', 'paragraph_2', 'quote_text')


@admin.register(FounderCollaborator)
class FounderCollaboratorAdmin(admin.ModelAdmin):
    list_display = ('name', 'role_title', 'organization', 'location', 'order', 'is_active', 'created_at')
    list_filter = ('organization', 'badge_theme', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    search_fields = ('name', 'role_title', 'organization', 'bio')


@admin.register(MethodologyPillar)
class MethodologyPillarAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'badge_color', 'order', 'is_active', 'created_at')
    list_filter = ('badge_color', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'tag', 'description', 'skills_list')


@admin.register(MindfulnessIntro)
class MindfulnessIntroAdmin(admin.ModelAdmin):
    list_display = ('headline', 'badge_text', 'safety_point_1_title', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    list_editable = ('is_active',)
    search_fields = ('headline', 'paragraph_1', 'paragraph_2', 'safety_point_1_title', 'safety_point_2_title')


@admin.register(CountryReach)
class CountryReachAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'country_code', 'badge_tag', 'order', 'is_active', 'created_at')
    list_filter = ('badge_tag', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    search_fields = ('country_name', 'country_code', 'description')


@admin.register(VolunteerStat)
class VolunteerStatAdmin(admin.ModelAdmin):
    list_display = ('label', 'number_value', 'subtitle', 'color_accent', 'order', 'is_active', 'created_at')
    list_display_links = ('label',)
    list_filter = ('color_accent', 'is_active', 'created_at')
    list_editable = ('number_value', 'subtitle', 'color_accent', 'order', 'is_active')
    search_fields = ('number_value', 'label', 'subtitle')


@admin.register(VolunteerRole)
class VolunteerRoleAdmin(admin.ModelAdmin):
    list_display = ('title', 'team_badge', 'color_theme', 'order', 'is_active', 'created_at')
    list_filter = ('team_badge', 'color_theme', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'team_badge', 'description', 'bullet_1', 'bullet_2')


@admin.register(VolunteerCountry)
class VolunteerCountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'country_code', 'flag_emoji', 'tag_label', 'order', 'is_active', 'created_at')
    list_display_links = ('name',)
    list_filter = ('is_active', 'created_at')
    list_editable = ('flag_emoji', 'tag_label', 'order', 'is_active')
    search_fields = ('name', 'country_code', 'tag_label')


@admin.register(VisionPillar)
class VisionPillarAdmin(admin.ModelAdmin):
    list_display = ('pillar_number', 'title', 'icon', 'accent_color', 'order', 'is_active', 'created_at')
    list_display_links = ('title',)
    list_filter = ('accent_color', 'is_active', 'created_at')
    list_editable = ('pillar_number', 'icon', 'accent_color', 'order', 'is_active')
    search_fields = ('title', 'description', 'pillar_number')


@admin.register(InvolvementTrack)
class InvolvementTrackAdmin(admin.ModelAdmin):
    list_display = ('track_number', 'title', 'badge_label', 'color_theme', 'order', 'is_active', 'created_at')
    list_display_links = ('title',)
    list_filter = ('color_theme', 'is_active', 'created_at')
    list_editable = ('track_number', 'badge_label', 'color_theme', 'order', 'is_active')
    search_fields = ('title', 'description', 'badge_label', 'commitment_info')


@admin.register(VolunteerJourneyStep)
class VolunteerJourneyStepAdmin(admin.ModelAdmin):
    list_display = ('step_number', 'title', 'icon_emoji', 'order', 'is_active', 'created_at')
    list_display_links = ('title',)
    list_filter = ('is_active', 'created_at')
    list_editable = ('step_number', 'icon_emoji', 'order', 'is_active')
    search_fields = ('title', 'description')


@admin.register(FAQItem)
class FAQItemAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'icon', 'order', 'is_active', 'created_at')
    list_display_links = ('question',)
    list_filter = ('category', 'is_active', 'created_at')
    list_editable = ('category', 'icon', 'order', 'is_active')
    search_fields = ('question', 'answer')
