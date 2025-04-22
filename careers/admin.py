from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import JobPost, JobApplication

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'job_type', 'location', 'is_active', 'posted_date', 'application_count')
    search_fields = ('title', 'department', 'location')
    list_filter = ('job_type', 'is_active', 'posted_date')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('posted_date',)
    list_editable = ('is_active',)
    
    def application_count(self, obj):
        count = obj.applications.count()
        url = reverse('admin:careers_jobapplication_changelist') + f'?job__id__exact={obj.id}'
        return format_html('<a href="{}">{} applications</a>', url, count)
    
    application_count.short_description = "Applications"

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_job_title', 'email', 'status', 'applied_date', 'resume_download')
    search_fields = ('name', 'email', 'job__title', 'position')
    list_filter = ('status', 'job', 'applied_date')
    readonly_fields = ('applied_date', 'updated_at')
    list_editable = ('status',)
    
    def get_job_title(self, obj):
        if obj.job:
            return obj.job.title
        return obj.position or "General Application"
    
    get_job_title.short_description = "Position/Job"
    get_job_title.admin_order_field = 'job__title'
    
    def resume_download(self, obj):
        if obj.resume:
            return format_html('<a href="{}" target="_blank">Download Resume</a>', obj.resume.url)
        return "No resume"
    
    resume_download.short_description = "Resume"