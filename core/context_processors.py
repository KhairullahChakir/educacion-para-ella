from .models import FooterSetting, FooterQuickLink, ContactSetting, SocialMediaLink


def site_settings(request):
    """Globally exposes footer settings, quick links, contact info, and social media to all templates."""
    footer_settings = FooterSetting.objects.filter(is_active=True).first()
    footer_quick_links = FooterQuickLink.objects.filter(is_active=True).order_by('order', '-created_at')
    global_contact_info = ContactSetting.objects.filter(is_active=True).first()
    
    footer_social_links = SocialMediaLink.objects.filter(is_active=True, show_in_footer=True).order_by('order', '-created_at')
    contact_social_links = SocialMediaLink.objects.filter(is_active=True, show_in_contact=True).order_by('order', '-created_at')
    all_social_links = SocialMediaLink.objects.filter(is_active=True).order_by('order', '-created_at')

    return {
        'footer_settings': footer_settings,
        'footer_quick_links': footer_quick_links,
        'global_contact_info': global_contact_info,
        'footer_social_links': footer_social_links,
        'contact_social_links': contact_social_links,
        'all_social_links': all_social_links,
    }
