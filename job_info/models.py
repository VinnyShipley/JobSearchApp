from django.db import models
from django.contrib.auth import get_user_model

class Job(models.Model):
  user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  company = models.CharField(max_length=256)
  title = models.CharField(max_length=256)
  location = models.CharField(max_length=50)
  salary_range = models.CharField(max_length=20)
  remote = models.BooleanField()
  hybrid = models.BooleanField()
  on_site = models.BooleanField()
  application_date = models.DateField(auto_now=False, auto_now_add=False)
  follow_up_date = models.DateField(auto_now=False, auto_now_add=False)
  connections = models.CharField(max_length=10)
  
  def __str__(self):
    return self.title
