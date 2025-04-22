from django.db import models
from ckeditor.fields import RichTextField

class JobPost(models.Model):
    JOB_TYPE_CHOICES = (
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    )
    
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    department = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    location = models.CharField(max_length=100)
    description = RichTextField()
    responsibilities = RichTextField()
    qualifications = RichTextField()
    salary_range = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    posted_date = models.DateField(auto_now_add=True)
    closing_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-posted_date']
# models.py
class JobApplication(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('reviewing', 'Reviewing'),
        ('shortlisted', 'Shortlisted'),
        ('interviewed', 'Interviewed'),
        ('offered', 'Offered'),
        ('rejected', 'Rejected'),
    )
    
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name='applications', null=True, blank=True)
    position = models.CharField(max_length=100, blank=True, null=True)  # For general applications
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    applied_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.job:
            return f"{self.name} - {self.job.title}"
        return f"{self.name} - {self.position or 'General Application'}"
    
    class Meta:
        ordering = ['-applied_date']