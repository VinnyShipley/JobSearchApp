from django.urls import path
from .views import JobCreateView, JobDeleteView, JobDetailView, JobListView

urlpatterns = [
  path('', JobListView.as_view(), name='job_list'),
  path('deatil/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
  path('delete/<int:pk>/', JobDeleteView.as_view(), name='job_delete'),
  path('create/', JobCreateView.as_view(), name='job_create')
]
