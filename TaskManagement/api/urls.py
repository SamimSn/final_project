from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'api'
urlpatterns = [
    path('', views.api_root, name='home'),
    path('tasks/', views.TaskListCreateView.as_view(), name='tasks_list_create_api'),
    path('task/<int:pk>', views.TaskDetailUpdateDeleteView.as_view(), name='task_retrieve_update_destroy_api'),
]
