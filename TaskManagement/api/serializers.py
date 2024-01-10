from rest_framework import serializers
from todo.models import Task

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        
class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description']
        
        
class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']