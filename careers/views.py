from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import JobPost, JobApplication
from .forms import JobApplicationForm

class JobListView(ListView):
    model = JobPost
    template_name = 'careers/job_list.html'
    context_object_name = 'jobs'
    queryset = JobPost.objects.filter(is_active=True)
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.http import HttpResponse
from django.views import View
from .models import JobPost, JobApplication
from .forms import JobApplicationForm
import logging

# Set up logging
logger = logging.getLogger(__name__)

class JobDetailView(View):
    template_name = 'careers/job_detail.html'
    
    def get_object(self, slug):
        return get_object_or_404(JobPost, slug=slug, is_active=True)
    
    def get(self, request, slug):
        job = self.get_object(slug)
        form = JobApplicationForm()
        context = {
            'job': job,
            'form': form,
            'jobs': JobPost.objects.filter(is_active=True).exclude(id=job.id)[:3]
        }
        return render(request, self.template_name, context)
    
    def post(self, request, slug):
        job = self.get_object(slug)
        form = JobApplicationForm(request.POST, request.FILES)
        
        # Debug information
        logger.debug(f"Form data: {request.POST}")
        logger.debug(f"Files: {request.FILES}")
        
        if form.is_valid():
            try:
                # Create but don't save yet
                application = form.save(commit=False)
                application.job = job
                application.save()
                
                messages.success(request, 'Your application has been submitted successfully.')
                return redirect('careers:job_detail', slug=slug)
            except Exception as e:
                # Log any errors
                logger.error(f"Error saving application: {str(e)}")
                messages.error(request, f"Error submitting application: {str(e)}")
        else:
            # Log validation errors
            logger.debug(f"Form errors: {form.errors}")
        
        # If we got here, there was an error
        context = {
            'job': job,
            'form': form,
            'jobs': JobPost.objects.filter(is_active=True).exclude(id=job.id)[:3]
        }
        return render(request, self.template_name, context)


class GeneralApplicationView(View):
    template_name = 'careers/job_list.html'
    
    def post(self, request):
        form = JobApplicationForm(request.POST, request.FILES)
        
        # Debug information
        logger.debug(f"General application form data: {request.POST}")
        logger.debug(f"Files: {request.FILES}")
        
        if form.is_valid():
            try:
                # Create but don't save yet
                application = form.save(commit=False)
                # Set the desired position from the form
                application.position = request.POST.get('position', 'General Application')
                application.save()
                
                messages.success(request, 'Your application has been submitted successfully.')
                return redirect('careers:job_list')
            except Exception as e:
                # Log any errors
                logger.error(f"Error saving general application: {str(e)}")
                messages.error(request, f"Error submitting application: {str(e)}")
        else:
            # Log validation errors
            logger.debug(f"Form errors: {form.errors}")
        
        # If we got here, there was an error
        context = {
            'jobs': JobPost.objects.filter(is_active=True),
            'form': form
        }
        return render(request, self.template_name, context)