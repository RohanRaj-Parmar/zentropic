from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Service, ServiceRequest
from .forms import ServiceRequestForm

class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'
    queryset = Service.objects.filter(is_active=True)

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ServiceRequestForm(initial={'service': self.object})
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ServiceRequestForm(request.POST)
        
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.service = self.object
            service_request.save()
            messages.success(request, 'Your service request has been submitted. We will contact you soon.')
            return redirect('services:service_detail', slug=self.object.slug)
        
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)