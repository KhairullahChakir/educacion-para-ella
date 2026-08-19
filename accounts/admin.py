from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, AuthSetting, AuthHighlight


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile & Role'


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'get_role', 'is_staff', 'is_superuser')

    def get_role(self, obj):
        if hasattr(obj, 'profile'):
            return obj.profile.get_role_display()
        return 'No Profile'
    get_role.short_description = 'Role'


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)


@admin.register(AuthSetting)
class AuthSettingAdmin(admin.ModelAdmin):
    list_display = ('headline', 'badge_label', 'quote_author', 'is_active', 'created_at')
    list_editable = ('is_active',)
    search_fields = ('headline', 'subheadline', 'student_quote')


@admin.register(AuthHighlight)
class AuthHighlightAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order', 'is_active', 'created_at')
    list_display_links = ('title',)
    list_editable = ('icon', 'order', 'is_active')
    search_fields = ('title', 'description')
