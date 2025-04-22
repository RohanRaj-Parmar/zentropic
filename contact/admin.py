from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('status', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('status',)
    ordering = ('-created_at',)