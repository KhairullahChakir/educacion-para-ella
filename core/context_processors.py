from .models import FooterSetting, FooterQuickLink, ContactSetting


def site_settings(request):
    """Globally exposes footer settings, quick links, and contact info to all templates."""
    footer_settings = FooterSetting.objects.filter(is_active=True).first()
    footer_quick_links = FooterQuickLink.objects.filter(is_active=True).order_by('order', '-created_at')
    global_contact_info = ContactSetting.objects.filter(is_active=True).first()
    
    return {
        'footer_settings': footer_settings,
        'footer_quick_links': footer_quick_links,
        'global_contact_info': global_contact_info,
    }
