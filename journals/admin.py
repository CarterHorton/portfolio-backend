from django.contrib import admin

from .models import projectEntry, journalEntry

# Register your models here.
admin.site.register(projectEntry)
admin.site.register(journalEntry)