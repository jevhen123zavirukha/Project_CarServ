from django.contrib import admin
from .models import About, AboutFeature


class AboutFeatureInline(admin.TabularInline):
    model = AboutFeature
    extra = 1
    

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_visible')
    list_filter = ('name', 'is_visible')
    search_fields = ('name', 'is_visible')


@admin.register(AboutFeature)
class AboutFeatureAdmin(admin.ModelAdmin):
    list_display = ('about', 'title', 'description')
    list_filter = ('order', )
    search_fields = ('description', )
