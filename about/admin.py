from django.contrib import admin
from .models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_visible')
    list_filter = ('name', 'is_visible')
    search_fields = ('name', 'is_visible')
