import datetime
from django.db import models
from django.conf import settings
from django import forms

# Create your models here.
class GeneratedURL(models.Model):
    """
        This model represents a shortened URL which has already been generated.
    """
    url = models.URLField(unique=True)
    date_generated = models.DateTimeField(auto_now_add=True)
    generated_alias = models.CharField(max_length=200, unique=True)

    def short_url(self):
        return settings.SITE_BASE_URL + self.to_base62()

    def __unicode__(self):
        return self.url  + '> ' + self.generated_alias

class LinkSubmitForm(forms.Form):
    u = forms.URLField(label='URL to be shortened:')

