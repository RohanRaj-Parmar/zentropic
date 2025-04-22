from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'email', 'phone', 'position', 'resume', 'cover_letter']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your.email@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+91 7433XXXXXX'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Desired Position'}),
            'resume': forms.FileInput(attrs={'class': 'form-control'}),
            'cover_letter': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your cover letter...', 'rows': 5}),
        }
        
    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume:
            # Check if the file is a PDF or DOC/DOCX
            file_extension = str(resume.name).split('.')[-1].lower()
            if file_extension not in ['pdf', 'doc', 'docx']:
                raise forms.ValidationError('Only PDF, DOC, or DOCX files are allowed.')
            # Limit file size to 5MB
            if resume.size > 5 * 1024 * 1024:
                raise forms.ValidationError('File size must be less than 5MB.')
        return resume

    def clean(self):
        cleaned_data = super().clean()
        # Add any cross-field validation here if needed
        return cleaned_data