from django.db import models
from ckeditor.fields import RichTextField

class Service(models.Model):
    SERVICE_TYPES = (
        ('ui_ux', 'UI/UX Design'),
        ('graphic', 'Graphic Design'),
        ('web', 'Website Development'),
        ('mobile', 'Mobile App Development'),
        ('digital', 'Digital Marketing'),
        ('social', 'Social Media Marketing'),
    )
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    short_description = models.TextField()
    description = RichTextField()
    icon = models.ImageField(upload_to='services/icons/')
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order']

class ServiceRequest(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected'),
    )
    
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='requests')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.service.name}"
    
    class Meta:
        ordering = ['-created_at']