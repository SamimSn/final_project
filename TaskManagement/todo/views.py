from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView, Response

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect,render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages

from .models import Task
from .forms import TaskCreateForm, TaskUpdateForm, searchForm

# Create your views here.

class RegisterView(SuccessMessageMixin, CreateView):    
    model = User
    template_name = 'registration/register.html'
    form_class =  UserCreationForm     
    success_message = "User added"
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)        
        for field in form.fields.keys():
            form[field].help_text = None
        return form
        

class TaskListCreateView(LoginRequiredMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'todo/task_list_create.html'    
    
    def get(self, request):      
        form_task = TaskCreateForm()  
        form_search = searchForm()
        search = request.GET.get('search')        
        if search:
            task_list = Task.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))
            form_search = searchForm(initial={'search': search})
            messages.success(request, f'search results for: {search}')
        else:
            task_list = Task.objects.all()
        context = {'task_list': task_list, 'form_task': form_task, 'form_search': form_search}
        return Response(context)       
    
    def post(self, request):
        form = TaskCreateForm(request.POST)
        if form.is_valid():            
            task = form.save(commit=False)
            task.owner = self.request.user            
            if not task.description:
                task.description = '-'            
            task.save()
            messages.success(request, 'Task added')
            return redirect(reverse('todo:list_create'))          
        tasks = Task.objects.all()
        return Response({'task_list': tasks, "form":form})
                        
    
class TaskDetailView(LoginRequiredMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'todo/task_detail.html'
    
    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except:            
            return render(request, 'todo/error.html', {'error':'Task not found!'})        
        context = {'task': task}
        return Response(context)
    

class TaskDeleteView(LoginRequiredMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'todo/task_confirm_delete.html'    
    
    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            if task.owner != self.request.user:
                return render(request, 'todo/error.html', {'error': 'This task does not belong to you!'})
        except:
            return render(request, 'todo/error.html', {'error': 'Task not found!'})
        return Response({'task': task})
    
    def post(self, request, pk):        
        task = get_object_or_404(Task, pk=pk)
        if task.owner == self.request.user:
            task.delete()
            messages.success(request, 'Task deleted')
        else:
            messages.error(request, 'You are not authorized to delete this task!')
        return redirect(reverse('todo:list_create'))    
        
class TaskUpdateView(LoginRequiredMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'todo/task_form.html'
    
    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)                        
            if task.owner != self.request.user:
                return render(request, 'todo/error.html', {'error': 'This task does not belong to you!'})
        except:
            return render(request, 'todo/error.html', {'error': 'Task not found!'})
        form = TaskUpdateForm(instance=task)
        return Response({'form': form})
    
    def post(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)                        
            if task.owner != self.request.user:
                return render(request, 'todo/error.html', {'error': 'This task does not belong to you!'})
        except:
            return render(request, 'todo/error.html', {'error': 'Task not found!'})
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():            
            if not task.description:
                task.description = '-'
            form.save()             
            messages.success(request, 'Task updated')
            return redirect(reverse('todo:list_create'))
        return redirect(reverse('todo:list_create'))    