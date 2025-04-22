from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import TeamMember, Testimonial, CompanyInfo
from services.models import Service

class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.filter(is_active=True)[:6]
        context['testimonials'] = Testimonial.objects.all()[:6]
        context['company_info'] = CompanyInfo.objects.first()
        return context

class AboutView(TemplateView):
    template_name = 'core/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_members'] = TeamMember.objects.all()
        context['company_info'] = CompanyInfo.objects.first()
        return context