from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = '👤 Student / Teacher Profile'
    fieldsets = (
        (None, {
            'fields': ('role', 'preferred_language', 'bio')
        }),
    )


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'get_role_badge', 'get_admin_badge', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'profile__role', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'profile__bio')
    fieldsets = (
        ('👤 Account Credentials', {
            'fields': ('username', 'password', 'email')
        }),
        ('📝 Personal Information', {
            'fields': ('first_name', 'last_name')
        }),
        ('🛡️ Permissions & Access Control', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('📅 Important Timestamps', {
            'fields': ('last_login', 'date_joined'),
            'classes': ('collapse',)
        }),
    )

    @admin.display(description='Role')
    def get_role_badge(self, obj):
        if hasattr(obj, 'profile'):
            role = obj.profile.role
            if role == 'teacher':
                return format_html('<span style="background: #e6fffa; color: #167888; border: 1px solid #99f6e4; font-weight: 800; font-size: 11px; padding: 3px 10px; border-radius: 9999px;">👩‍🏫 Teacher</span>')
            return format_html('<span style="background: #fef3c7; color: #92400e; border: 1px solid #fde68a; font-weight: 800; font-size: 11px; padding: 3px 10px; border-radius: 9999px;">🎓 Student</span>')
        return format_html('<span style="color: #94a3b8; font-size: 11px;">No Profile</span>')

    @admin.display(description='Permissions')
    def get_admin_badge(self, obj):
        if obj.is_superuser:
            return format_html('<span style="background: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff; font-weight: 800; font-size: 11px; padding: 3px 10px; border-radius: 9999px;">👑 Superadmin</span>')
        elif obj.is_staff:
            return format_html('<span style="background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; font-weight: 800; font-size: 11px; padding: 3px 10px; border-radius: 9999px;">🛡️ Staff Admin</span>')
        return format_html('<span style="color: #64748b; font-size: 11px; font-weight: 600;">Member</span>')


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
