from django.contrib import admin
from .models import Show

#admin.site.register(Show)

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ("id", "kategorie", "genre", "artist", "ort", "location", "kosten", "jahr")
