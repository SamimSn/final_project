from django.urls import path, reverse_lazy
from . import views

app_name = 'todo'
urlpatterns = [    
    path('register/', views.RegisterView.as_view(success_url=reverse_lazy('login')) , name='register'),  
    path('', views.TaskListCreateView.as_view(), name='list_create'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='detail'),
    path('<int:pk>/edit', views.TaskUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', views.TaskDeleteView.as_view(), name='delete'),     
]