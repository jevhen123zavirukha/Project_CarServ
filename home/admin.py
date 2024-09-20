from django.contrib import admin
from .models import Establishment


@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email', 'is_visible')
    list_filter = ('name', 'phone', 'email', 'is_visible')
    search_fields = ('name', 'address', 'phone', 'email', 'is_visible')
