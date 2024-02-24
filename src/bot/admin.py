from django.contrib import admin

from bot.models import User, Section, SectionItem

admin.site.register(User)
admin.site.register(Section)
admin.site.register(SectionItem)
