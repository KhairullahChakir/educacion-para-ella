from django.contrib import admin
from .models import HeroNews


@admin.register(HeroNews)
class HeroNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'badge_text', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'subtitle', 'badge_text')
