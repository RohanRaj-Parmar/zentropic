from django.contrib import admin
from .models import TeamMember, Testimonial, CompanyInfo

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'order')
    search_fields = ('name', 'position')
    list_filter = ('position',)
    ordering = ('order',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'order')
    search_fields = ('name', 'company')
    ordering = ('order',)

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'phone')
    
    def has_add_permission(self, request):
        # Check if any CompanyInfo object exists
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)