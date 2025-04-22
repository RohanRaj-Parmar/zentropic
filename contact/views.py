from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import ContactMessage
from .forms import ContactForm
from core.models import CompanyInfo
from django.core.mail import send_mail
from django.conf import settings


class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:thank_you')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_info'] = CompanyInfo.objects.first()
        return context
    
    def form_valid(self, form):
        contact_message = form.save(commit=True) 
        company_info = CompanyInfo.objects.first()
        if company_info:
            admin_email = company_info.email
            try:
                send_mail(
                    subject=f'New Contact Message: {form.cleaned_data["subject"]}',
                    message=f'You have received a new contact message from {form.cleaned_data["name"]}.\n\n'
                            f'Email: {form.cleaned_data["email"]}\n'
                            f'Phone: {form.cleaned_data["phone"]}\n\n'
                            f'Message:\n{form.cleaned_data["message"]}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[admin_email],
                )
            except Exception as e:
                # Log the error but still save the message to database
                print(f"Email sending error: {e}")

        messages.success(self.request, 'Your message has been sent successfully. We will get back to you soon.')
        return super().form_valid(form)

class ThankYouView(TemplateView):
    template_name = 'contact/thank_you.html'
