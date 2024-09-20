from django.contrib import admin
from .models import ContactInfo, MessageFromCustomer, Subscriber


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'is_visible')
    list_filter = ('is_visible', )
    list_editable = ('is_visible',)


@admin.register(MessageFromCustomer)
class MessageFromCustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'updated_at')
    list_filter = ('created_at', )
    list_editable = ('subject', 'email',)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', )
    list_editable = ('is_active',)
