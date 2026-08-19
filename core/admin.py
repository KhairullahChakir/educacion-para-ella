from django.contrib import admin
from .models import HeroNews, ClassProgram, HowItWorksStep, Partner


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
