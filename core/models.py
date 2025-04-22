from django.db import models
from ckeditor.fields import RichTextField

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='team/')
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order']

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    quote = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.name} - {self.company}"
    
    class Meta:
        ordering = ['order']

class CompanyInfo(models.Model):
    company_name = models.CharField(max_length=100, default="Zentropic Software Solution")
    tagline = models.CharField(max_length=200)
    about_short = models.TextField()
    about_long = RichTextField()
    mission = RichTextField()
    vision = RichTextField()
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.company_name
    
    class Meta:
        verbose_name_plural = "Company Information"