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
