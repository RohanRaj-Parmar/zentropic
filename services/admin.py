from django.contrib import admin
from .models import Service, ServiceRequest

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_type', 'order', 'is_active')
    search_fields = ('name', 'short_description')
    list_filter = ('service_type', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('order',)

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service', 'status', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('status', 'service', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('status',)
    ordering = ('-created_at',)