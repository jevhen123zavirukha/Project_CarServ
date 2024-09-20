from django.contrib import admin
from .models import Service
from django.utils.safestring import mark_safe


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('photo_tag', 'name', 'description', 'is_visible')
    list_filter = ('is_visible', )

    def photo_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50"  height="50"/>')

    photo_tag.short_description = 'Logo'
