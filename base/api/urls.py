from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview),                      # API overview
    path('task-list/', views.task_list),                # Get a list of all tasks
    path('task-detail/<str:pk>/', views.task_detail),   # Get details of a specific task
    path('task-create/', views.task_create),            # Create a new task
    path('task-update/<str:pk>/', views.task_update),   # Update an existing task
    path('task-delete/<str:pk>/', views.task_delete),   # Delete a task
]
