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
