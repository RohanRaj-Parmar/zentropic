from django.urls import path
from . import views

app_name = 'careers'

urlpatterns = [
    path('', views.JobListView.as_view(), name='job_list'),
    path('apply/', views.GeneralApplicationView.as_view(), name='general_application'),
    path('<slug:slug>/', views.JobDetailView.as_view(), name='job_detail'),
]