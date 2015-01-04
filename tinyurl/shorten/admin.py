from django.contrib import admin

from models import GeneratedURL

class GeneratedURLAdmin(admin.ModelAdmin):
    model = GeneratedURL
    extra = 3

admin.site.register(GeneratedURL, GeneratedURLAdmin)