from django.shortcuts import render
from .models import Job
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.urls import reverse_lazy

class JobListView(ListView):
  template_name = 'job_list.html'
  model = Job

class JobDetailView(DetailView):
  template_name = 'job_detail.html'
  model = Job

class JobCreateView(CreateView):
  template_name = 'job_create.html'
  model = Job
  fields = ['company', 'title', 'location', 'salary_range', 'remote', 'hybrid', 'on_site', 'application_date', 'follow_up_date', 'connections']

class JobDeleteView(DeleteView):
  template_name = 'job_delete.html'
  model = Job
  success_url = reverse_lazy('job_list')
