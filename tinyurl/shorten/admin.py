from django.contrib import admin

from models import GeneratedURL, WordBank

class GeneratedURLAdmin(admin.ModelAdmin):
    model = GeneratedURL
    extra = 3

class WordBankAdmin(admin.ModelAdmin):
    list_display = ['id', 'word', 'taken']
    pass


admin.site.register(GeneratedURL, GeneratedURLAdmin)
admin.site.register(WordBank, WordBankAdmin)